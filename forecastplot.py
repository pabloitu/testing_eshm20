import csep

import matplotlib.pyplot as plt
from hazard2csep.forecast_lib import read_forecast
import cartopy
import os


for i in os.walk('models/forecasts', topdown=True):
    for j in i[2]:
        if j.endswith('.csv'):
            a = read_forecast(f'models/forecasts/{j}')
            fig = plt.figure(figsize=(12,6))
            ax = fig.add_subplot(111, projection=cartopy.crs.PlateCarree())

            a.plot(ax=ax,
                   plot_args={'region_border': False,
                              'title': j.split('.')[0]} )
            plt.show()