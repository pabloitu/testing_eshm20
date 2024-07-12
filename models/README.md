
## Model access and reading

This environment should be run with conda, outside the top `floatcsep` environment. If you do not have conda installed, please follow the instructions [here](https://docs.conda.io/en/latest/miniconda.html). 

```shell
git clone git@github.com:cseptesting/hazard2csep.git --depth=1 --branch=main 
rm -rf ./hazard2csep/.git
# todo change name from oq2csep to hazard2csep 
cd hazard2csep
conda env create -f environment.yml
conda activate hazard2csep
pip install -e .
```


## Download related data

Download ESHM20 (Danciu et al., 2021)

```shell
git clone https://gitlab.seismo.ethz.ch/efehr/eshm20 --depth=1
```

Download ESHM13 (Woessner et al., 2015)
```shell
wget http://hazard.efehr.org/export/sites/efehr/.galleries/dwl_europe2013/SHARE_OQ_input_20140807.zip_2063069299.zip -O temp.zip && unzip temp.zip -d eshm13 && rm temp.zip 
unzip eshm13/SHARE_OQ_input_20140807/source_models.zip -d eshm13/SHARE_OQ_input_20140807/

```


## References and Links

* pyCSEP: https://github.com/SCECcode/pycsep


Savran, W. H., Bayona, J. A., Iturrieta, P., Asim, K. M., Bao, H., Bayliss, K., Herrmann, M., Schorlemmer, D., Maechling, P. J. & Werner, M. J. (2022). pyCSEP: A python toolkit for earthquake forecast developers. Seismological Research Letters, 93(5), 2858-2870. https://doi.org/10.1785/0220220033

* OpenQuake: https://github.com/gem/oq-engine

Pagani, M., Monelli, D., Weatherill, G., Danciu, L., Crowley, H., Silva, V., ... & Vigano, D. (2014). OpenQuake engine: An open hazard (and risk) software for the global earthquake model. Seismological Research Letters, 85(3), 692-702.


* The 2013 European Seismic Hazard Model

Woessner, J., Danciu L., D. Giardini and the SHARE consortium (2015), The 2013 European Seismic Hazard Model: key components and results, Bull. Earthq. Eng., doi:10.1007/s10518-015-9795-1.

* The 2020 European Seismic Hazard Model:

Danciu L., Nandan S., Reyes C., Basili R., Weatherill G., Beauval C., Rovida A., Vilanova S., Sesetyan K., Bard P-Y., Cotton F., Wiemer S., Giardini D. (2021) - The 2020 update of the European Seismic Hazard Model: Model Overview. EFEHR Technical Report 001, v1.0.0, https://doi.org/10.12686/a15

