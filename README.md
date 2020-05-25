A. What is in this directory:
1. git souce from repo https://github.com/CSSEGISandData/COVID-19.git
2. Data update regularly from Johns Hopkins on Covid19 stat. 
   This data set is the basis of Johns Hopkins real-time dashboard on Covid19 around the work.
3. Jupyter python notebook by CW Chung to display the covid19 of coutries, provices/states, and counties of interest.
   The POI can be customized easily to display different countries, states, counties.

B. Setting up:
1. Git. Pls download and set up git if you don;t already have it.
   Run the following command to get the source and data  from the COVID-19 project
   $ git https://github.com/CSSEGISandData/COVID-19.git
   The data will be refreshed every day. To update, just do: $ git pull in this directory.
2. Anaconda setup. I recommend installing miniconda, and then set up your own conda env with
   the required python packages (numpy, pandas, matplotlib, seaborn, plotly). You can use an IDE,
   but I found that using Jupyter notebook is just as convenient.
   * download miniconda for your env
   * install miniconda (preferably in /opt/conda, but could be any where)
   * run this to use with miniconda:
     $ source /opt/conda/etc/profile.d/conda.sh (replace /opt/conda with conda installation directory)
     $ conda activate base   ## just to make sure your miniconda is set up properly
     $ conda env list        ## should show base
     $ conda list            ## show the python packages installed in base. Should be about 20 to 40.
     $ python --version      ## show the version of python in the base env. Your env python could be of diff version from base
     $ conda create -n covid python=3.6  anaconda  ## create new conda env named covid, python=3.6, anaconda jumbo packages
     $ conda env list        ## now should show both base and covid.
     $ conda activate covid  ## use covid as your default env
     $ conda list            ## now you see a few hundred packages, inluding jupyter, numpy, pandas, matplotlib
     $ conda install plotly seaborn   ## install both if not already in anaconda.
     $ python --version      ## should show 3.6.x. This version is going to be different from python in the base.

3. After git clone setting up the project, copy CW workbook to csse_covid_19_data/csse_covid_19_time_series
   This is the directory where the data files will be. For convenience, I just run jupyter there.
4. You can also use Makefile at the COVID-19 top directory. 
   * make data               ## to git pull and sync the latest data files
   * make sample-covid       ## Update the makefile to activate the right conda env, then bring up jupyter lab.
5. After jupyter lab is running, File-Open the workbook WIP-CW-COVID19.ipyn 
6. Make a copy and/or use a new name for your workbook.

C. The workbookd WIP-CW-COVID19.ipynb

* Covid19 Coronairus Cases Data and Visualization
  * Data obtained from Johns Hopkins (refreshed periodically)
  * US Data at both county level and state level (so need to dedup to calculate total)
  * Worldwide data mostly at country level, except US, China, Canada, Australia at state/province level
  * Original data: all cumulative: confirmed, death, recovered.
  * Also Chinese Data from Ding Xiang Yuan which provide city level data for China.
  * Real Time Dashboard here: https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6
* Data Source: two CSV files on Confirmed Cases:
  GBL_CONF_CSV = "time_series_covid19_confirmed_global.csv"	# country, with state/province for US, China, Canada, Australia.
  US_CONF_CSV =  "time_series_covid19_confirmed_US.csv"		# US at county level
  There are csv files for death and recovered patients, but they are not being used at this moment.
* Data Structures:
  * Data Frames: incr DFs are derived from aggr data frame. _aggr is aggregated by country (or by an ID).
     * gbl_conf_aggr : global cum confirmed aggregated by country. Index == country. First column is 1/24 data
     * gbl_conf_incr : global daily confirmed aggregated by country. Index == country. First column is 1/24 data
     * us_conf_aggr : US State confirmed aggregated by state. Index == state. First column is 1/24 data
     * us_conf_incr : US State daily confirmed aggregated by state. Index == state. First column is 1/24 data
     * county_conf_aggr : County confirmed aggregated by CombinedKey Index == county. First column is 1/24 data
     * county_conf_incr : County daily confirmed aggregated by CombinedKey. Index == county. First column is 1/24 data
  * COL_LIST: columnn names  (many in the form of 3/24, 5/13)
    DT_LIST (and dt_list): replace the column name by datetime, so that plot functions will handle the displat correctlt.

* Helper functions:
  * Data cleansing:  rename some columns. Also dropping several columns after aggr (and thefore incr too).
* Plotting Functions:
  1. plot_bar: bar graph plot (usually for daily incremental new cases)
  2. plot_line: line plot (usually for cumulative confirmed cases)
  3. plot_bar_line: plot both on the same graph. Support logy=True to plot cum case in log
  4. plot_entity_util: pass in the DFs and plot (e.g. global confirmed cases, state/province cases, county cases)
     key param: DFs, logy, lastn: last -N days (e.g lastn=-30 for the last 30 days).
  5. plot_4_entity_confirmed: display 4 different countries/states/counties. Can display cum confirmed and/or daily increment
     (note: seem to have a bug in display of cumulative cases)
     e.g. set up to display: Spain, Italy, Germany, France;  NY, NJ, Connecticut, California
  6. Display NYC (NY+NJ+Connecticut), and non-NYC state
  7. Calc_multiple: calculate various metrics, display in a table form 
     Typically called with -15 for a week to week analysis for the last two weeks
               Entity,   4/11/20,  4/18/20,    4/25/20,   ratio1,  ratio2, rate of growth per week 
	Entity	Num_Begin	Num_Mid	Num_End	Delta1	Delta2	Ratio_m2b	Ratio_e2m	Ratio_e2b	WCGrowth	Ratio_w2w
	0	US	526396	732197	938154	205801	205957	1.39	1.28	1.78	1.33	1.00
	1	Spain	163027	191726	223759	28699	32033	1.18	1.17	1.37	1.17	1
    * Can work at country level, state level or county level
    * Also at a region level such as Bay Area which includes the 9 countries, plus 4 around Sacramento, and Santa Cruz
* Save  in pdf
  I used to be able to save the figures and tables in pdf files. That function needs to be added back.
  Saving in pdf file is useful if you want to send/share the output.

**  files:
./Makefile
./README.md
./Getting-Started.txt
./who_covid_19_situation_reports
./who_covid_19_situation_reports/who_covid_19_sit_rep_time_series
./who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/who_covid_19_sit_rep_time_series.csv
./who_covid_19_situation_reports/README.md
./who_covid_19_situation_reports/who_covid_19_sit_rep_pdfs
./who_covid_19_situation_reports/who_covid_19_sit_rep_pdfs/20200309-sitrep-49-covid-19.pdf
./who_covid_19_situation_reports/who_covid_19_sit_rep_pdfs/20200321-sitrep-61-covid-19.pdf
./csse_covid_19_data
./csse_covid_19_data/csse_covid_19_time_series
./csse_covid_19_data/csse_covid_19_time_series/2020-0426
./csse_covid_19_data/csse_covid_19_time_series/2020-0426/time_series_covid19_confirmed_global.csv
./csse_covid_19_data/csse_covid_19_time_series/2020-0426/time_series_covid19_confirmed_US.csv
./csse_covid_19_data/csse_covid_19_time_series/2020-0426/Errata.csv
./csse_covid_19_data/csse_covid_19_time_series/2020-0426/time_series_covid19_recovered_global.csv
./csse_covid_19_data/csse_covid_19_time_series/2020-0426/time_series_covid19_deaths_global.csv
./csse_covid_19_data/csse_covid_19_time_series/2020-0426/time_series_covid19_deaths_US.csv
./csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
./csse_covid_19_data/csse_covid_19_time_series/WIP-CW-COVID19.ipynb
./csse_covid_19_data/csse_covid_19_time_series/Untitled.ipynb
./csse_covid_19_data/csse_covid_19_time_series/Makefile
./csse_covid_19_data/csse_covid_19_daily_reports_us/04-24-2020.csv
./csse_covid_19_data/README.md
./csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv
./csse_covid_19_data/csse_covid_19_daily_reports
./csse_covid_19_data/csse_covid_19_daily_reports/02-26-2020.csv
.
