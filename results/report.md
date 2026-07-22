<div style='overflow:auto;'>
  <img src='../../../miniforge3/envs/testing_eshm20/lib/python3.12/site-packages/floatcsep/postprocess/artifacts/logo.png' class='figure-img' style='float:right; margin-left:1em; width:130px; height:auto;' />
  <h1 style='margin:0;'><a id='experiment_report'></a>Experiment Report</h1>
  <p style='margin:0; font-size:1.6em;'>ESHM20 Testing</p>
</div>

## Table of Contents
1. [Experiment metadata](#experiment_metadata)
1. [Objectives](#objectives)
1. [Authoritative Data](#authoritative_data)
1. [Forecasts](#forecasts)
1. [Test results](#test_results)

This experiment evaluates the performance of earthquake forecast models within a fully specified and reproducible testing framework. This report summarizes the main results.

## Experiment metadata <a id="experiment_metadata"></a>


- **Start date:** 2015-01-01 00:00:00
- **End date:** 2022-01-01 00:00:00
- **Class:** Time-Independent
- **Magnitude range:** 4.9 ≤ Mw ≤ 8.9
- **Region:** region_europe.txt
- **Catalog:** emec_catalog.json
- **Models:** SEIFA13, FSBG13, ASM13, FSM20@SRU_MU, FSM20@SRU_ML, FSM20@SRU_MA, FSM20@SRL_MU, FSM20@SRL_ML, FSM20@SRL_MA, FSM20@SRA_MU, FSM20@SRA_ML, FSM20@SRA_MA, ASM20@Pareto_Mc_upp, ASM20@Pareto_Mc_mid, ASM20@Pareto_Mc_low, ASM20@TGR_mid_Mmax_upp, ASM20@TGR_mid_Mmax_mid, ASM20@TGR_mid_Mmax_low, ASM20@TGR_lo_Mmax_upp, ASM20@TGR_lo_Mmax_mid, ASM20@TGR_lo_Mmax_low, ASM20@TGR_hi_Mmax_upp, ASM20@TGR_hi_Mmax_mid, ASM20@TGR_hi_Mmax_low
- **Evaluations:** Poisson_N, Poisson_S, Poisson_M, Poisson_T

## Objectives <a id="objectives"></a>


* Ensure transparent and reproducible evaluation of submitted models.
* Compare forecasts against authoritative seismicity observations.

## Authoritative Data <a id="authoritative_data"></a>


### Input catalog  <a id="input_catalog"></a>



<img src="catalog.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>
<img src="events.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>


Evaluation catalog from 2015-01-01 00:00:00 until 2022-01-01 00:00:00. Earthquakes are filtered above Mw 4.9.
## Forecasts <a id="forecasts"></a>


### SEIFA13  <a id="seifa13"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_SEIFA13.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSBG13  <a id="fsbg13"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSBG13.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM13  <a id="asm13"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM13.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRU_MU  <a id="fsm20@sru_mu"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRU_MU.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRU_ML  <a id="fsm20@sru_ml"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRU_ML.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRU_MA  <a id="fsm20@sru_ma"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRU_MA.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRL_MU  <a id="fsm20@srl_mu"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRL_MU.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRL_ML  <a id="fsm20@srl_ml"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRL_ML.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRL_MA  <a id="fsm20@srl_ma"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRL_MA.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRA_MU  <a id="fsm20@sra_mu"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRA_MU.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRA_ML  <a id="fsm20@sra_ml"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRA_ML.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### FSM20@SRA_MA  <a id="fsm20@sra_ma"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_FSM20@SRA_MA.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@Pareto_Mc_upp  <a id="asm20@pareto_mc_upp"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@Pareto_Mc_upp.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@Pareto_Mc_mid  <a id="asm20@pareto_mc_mid"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@Pareto_Mc_mid.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@Pareto_Mc_low  <a id="asm20@pareto_mc_low"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@Pareto_Mc_low.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_mid_Mmax_upp  <a id="asm20@tgr_mid_mmax_upp"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_mid_Mmax_upp.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_mid_Mmax_mid  <a id="asm20@tgr_mid_mmax_mid"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_mid_Mmax_mid.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_mid_Mmax_low  <a id="asm20@tgr_mid_mmax_low"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_mid_Mmax_low.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_lo_Mmax_upp  <a id="asm20@tgr_lo_mmax_upp"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_lo_Mmax_upp.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_lo_Mmax_mid  <a id="asm20@tgr_lo_mmax_mid"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_lo_Mmax_mid.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_lo_Mmax_low  <a id="asm20@tgr_lo_mmax_low"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_lo_Mmax_low.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_hi_Mmax_upp  <a id="asm20@tgr_hi_mmax_upp"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_hi_Mmax_upp.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_hi_Mmax_mid  <a id="asm20@tgr_hi_mmax_mid"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_hi_Mmax_mid.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



### ASM20@TGR_hi_Mmax_low  <a id="asm20@tgr_hi_mmax_low"></a>



<img src="2015-01-01_2022-01-01/figures/forecast_ASM20@TGR_hi_Mmax_low.png" class="figure-img" style="display:block; margin:0.5em auto; width:90%; max-width:100%; height:auto;" width="720"/>



## Test results <a id="test_results"></a>


### Poisson_N  <a id="poisson_n"></a>



<img src="2015-01-01_2022-01-01/figures/Poisson_N.png" class="figure-img" style="display:block; margin:0.5em auto; width:75%; max-width:100%; height:auto;" width="600"/>



### Poisson_S  <a id="poisson_s"></a>



<img src="2015-01-01_2022-01-01/figures/Poisson_S.png" class="figure-img" style="display:block; margin:0.5em auto; width:75%; max-width:100%; height:auto;" width="600"/>



### Poisson_M  <a id="poisson_m"></a>



<img src="2015-01-01_2022-01-01/figures/Poisson_M.png" class="figure-img" style="display:block; margin:0.5em auto; width:75%; max-width:100%; height:auto;" width="600"/>



### Poisson_T  <a id="poisson_t"></a>



<img src="2015-01-01_2022-01-01/figures/Poisson_T.png" class="figure-img" style="display:block; margin:0.5em auto; width:75%; max-width:100%; height:auto;" width="600"/>



