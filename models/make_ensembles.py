import numpy as np
from os.path import join
import csep
import hazard2csep
import os


lt_eshm13 = [('eshm13_as.csv', 0.5),  # to do real vals
             ('eshm13_fsbg.csv', 0.3),
             ('eshm13_seifa.csv', 0.2)]

# component weights
uas = 0.5
fssm = 0.5

tr = 0.6
abl = 0.2
abm= 0.6
abu = 0.2

ml = 0.5
ma = 0.4
mu = 0.1

paretto = 0.4

srl = 0.1
sra = 0.5
sru = 0.4

lt_eshm20 = [('ABL_ML.csv', uas*tr*abl*ml),
           ('ABL_MC.csv', uas*tr*abl*ma),
           ('ABL_MU.csv', uas*tr*abl*mu),
           ('ABM_ML.csv', uas*tr*abm*ml),
           ('ABM_MC.csv', uas*tr*abm*ma),
           ('ABM_MU.csv', uas*tr*abm*mu),
           ('ABU_ML.csv', uas*tr*abu*ml),
           ('ABU_MC.csv', uas*tr*abu*ma),
           ('ABU_MU.csv', uas*tr*abu*mu),
           ('PM_ML.csv', uas*paretto*ml),
           ('PM_MC.csv', uas*paretto*ma),
           ('PM_MU.csv', uas*paretto*mu),
           ('fs_SRL_ML.csv', fssm*srl*ml),
           ('fs_SRL_MA.csv', fssm*srl*ma),
           ('fs_SRL_MU.csv', fssm*srl*mu),
           ('fs_SRA_ML.csv', fssm*sra*ml),
           ('fs_SRA_MA.csv', fssm*sra*ma),
           ('fs_SRA_MU.csv', fssm*sra*mu),
           ('fs_SRU_ML.csv', fssm*sru*ml),
           ('fs_SRU_MA.csv', fssm*sru*ma),
           ('fs_SRU_MU.csv', fssm*sru*mu)]


eshm13_data = []
for comp in lt_eshm13:
    model = hazard2csep.forecast_lib.read_forecast(join('forecasts', comp[0]))
    eshm13_data.append((model.data, comp[1]))

rates_ = np.zeros(eshm13_data[0][0].shape)
for i in eshm13_data:
    rates_ += i[0] * i[1]

eshm13 = csep.forecasts.GriddedForecast(data=rates_, region=model.region, magnitudes=model.magnitudes)
eshm13.plot(show=True)




eshm20_data = []
for comp in lt_eshm20:
    model = hazard2csep.forecast_lib.read_forecast(join('forecasts', comp[0]))
    eshm20_data.append((model.data, comp[1]))
rates_ = np.zeros(eshm20_data[0][0].shape)
for i in eshm20_data:
    rates_ += i[0] * i[1]

eshm20 = csep.forecasts.GriddedForecast(data=rates_, region=model.region, magnitudes=model.magnitudes)
eshm20.plot(show=True)
