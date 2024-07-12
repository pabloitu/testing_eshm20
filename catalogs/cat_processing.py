import csep
from datetime import datetime, timedelta
from csep.utils.time_utils import datetime_to_utc_epoch
import numpy as np
import matplotlib.pyplot as plt
from openquake.hmtk.seismicity.declusterer import dec_gardner_knopoff
from openquake.hmtk.seismicity.declusterer import distance_time_windows
from openquake.hmtk.seismicity import catalogue, selector
from csep.core.regions import CartesianGrid2D

def cat_oq2csep(cat_oq, region=None):

    times = cat_oq.get_decimal_time()
    year = times.astype(int)
    rem = times - year
    base = [datetime(y, 1, 1) for y in year]
    datetimes = [b + timedelta(seconds=(b.replace(year=b.year + 1) - b).total_seconds() * r) for b, r in
                 zip(base, rem)]

    out = []
    for n, time_i in enumerate(datetimes):
        event_tuple = (n,
                       csep.utils.time_utils.datetime_to_utc_epoch(time_i),
                       cat_oq['latitude'][n],
                       cat_oq['longitude'][n],
                       cat_oq['depth'][n],
                       np.round(cat_oq['magnitude'][n], 1)
                       )
        out.append(event_tuple)

    cat = csep.catalogs.CSEPCatalog(data=out, region=region)

    return cat

def cat_csep2oq(catalog):

    id_ = catalog.get_event_ids().astype(int)
    datetimes = catalog.get_datetimes()
    year = np.array([i.year for i in datetimes])
    month = np.array([i.month for i in datetimes])
    day = np.array([i.day for i in datetimes])
    hour = np.array([i.hour for i in datetimes])
    minute = np.array([i.minute for i in datetimes])
    second = np.array([i.second for i in datetimes])

    lat = catalog.get_latitudes()
    lon = catalog.get_longitudes()
    depth = catalog.get_depths()
    mag = catalog.get_magnitudes()

    data = np.vstack((id_, year, month, day, hour, minute, second, lon, lat,
                      depth, mag)).T

    cat = catalogue.Catalogue()
    cat.load_from_array(
        ['eventID', 'year', 'month', 'day', 'hour', 'minute',
         'second', 'longitude', 'latitude', 'depth', 'magnitude'],
        data)

    cat.update_end_year()
    cat.update_start_year()

    cat.name = 'emec'
    cat.sort_catalogue_chronologically()

    return cat


def read_raw_cat(start_time=datetime(2014, 1,1),
                 end_time=datetime(2022,1,1),
                 min_mag=4.7, max_depth=30, plot=False,
                 region=False):
    # read the catalog
    cat = np.genfromtxt('EMEC-2021_events.csv', delimiter=',',
                        skip_header=0, names=True, dtype=None, encoding=None)
    ids = cat['event_id']
    year = cat['year']
    month = [i if i > 0 else 1 for i in cat['month']]
    day = [i if i > 0 else 1 for i in cat['day']]
    hour = [i if i > 0 else 1 for i in cat['hour']]
    minute = [i if i > 0 else 1 for i in cat['minute']]
    seconds = [int(np.floor(i)) if (i > 0 and i < 60) else 1 for i in cat['second']]
    epochs = [datetime_to_utc_epoch(datetime(y, m, s, h, mi, ss)) for
                                     y, m, s, h, mi, ss in
                                     zip(year, month, day, hour, minute,
                                         seconds)]
    mw = cat['mw']
    lat = cat['latitude']
    lon = cat['longitude']
    depth = cat['depth']

    events = [(id_, epoch, lat_, lon_, depth_, mw_) for
              id_, epoch, lat_, lon_, depth_, mw_ in
              zip(ids, epochs, lat, lon, depth, mw)]

    cat = csep.catalogs.CSEPCatalog(data=events)

    cat.filter([f'origin_time >= {datetime_to_utc_epoch(start_time)}',
                f'origin_time <= {datetime_to_utc_epoch(end_time)}',
                f'magnitude >= {min_mag}',
                f'depth <= {max_depth}'],
               in_place=True)

    if region:

        region_csep = CartesianGrid2D.from_origins(np.genfromtxt(region), dh=0.1)

        cat.filter_spatial(region_csep, in_place=True)

    print(f'Catalog contains {cat.get_number_of_events()} events')

    cat.write_ascii('EMEC.csv')
    if plot:
        cat.plot(plot_args={'region_border': False})
        plt.show()
    return cat


def decluster_gk(catalog, plot=False):

    params = {'time_distance_window': distance_time_windows.GruenthalWindow(),
              'fs_time_prop': 0.1}

    catalogue = cat_csep2oq(catalog)
    declusterer = dec_gardner_knopoff.GardnerKnopoffType1()
    cluster, val = declusterer.decluster(catalogue, params)

    is_valid = np.array([True if i == 0 else False for i in val])

    select = selector.CatalogueSelector(catalogue)

    dc_cat = select.select_catalogue(is_valid)
    dc_cat_csep = cat_oq2csep(dc_cat)

    dc_cat_csep.write_ascii('EMEC_dec_grunthal.csv')

    print('Declustered catalog contains {} events'.format(dc_cat_csep.get_number_of_events()))

    if plot:
        ax = catalog.plot(plot_args={'markercolor': 'red'})
        dc_cat_csep.plot(ax=ax, extent=[10, 15, 35, 45], plot_args={'markercolor': 'blue'})
        plt.show()
    return dc_cat_csep


catalog_ndc = read_raw_cat(region='../models/regions/region_final.txt', plot=True)
a = decluster_gk(catalog_ndc)


