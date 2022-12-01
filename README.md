# Data Science Fall 2022
### Group 3 - Los Pollos Hermanos
Dean Vogel, Julian Lioanag, Nathan Agpalo, Bill Ni

Optimal placement of renewable energy sources (wind, solar, geothermal) based on energy strength, energy consumption, distance to populated areas, crime rate, natural disaster frequency, and other notable factors.

## Data Sources
### Population
Datafile: [gpw_pop.asc](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/population_count/gpw_pop.asc.zip)

 - Data is for 2020 values
 - Datafile is zipped, unzip to view properly
 - Datafile is ASCII format, printed as space-separated values, where each number is a value for that pixel in 8640 by 4320 grid

Sourced from: [NASA SEDAC](https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-rev11)

### Wind Speed
Datafile: [avg_wind_speed.nc](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/energy_strength/wind/avg_wind_speed.nc)

 - Data is from 2012 to 2022
 - Datafile is NetCDF format, tracking average wind speed on surface

Sourced from: [NASA Giovanni](https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=2012-11-01T00:00:00Z&endtime=2022-11-30T23:59:59Z&data=M2TMNXFLX_5_12_4_SPEED)

### Solar Energy (Incident Surface Shortwave Radiation)
Datafile: [avg_wind_speed.nc](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/energy_strength/wind/avg_solar_energy.nc)

 - Data is from 2019-01-01 to 2022-11-30
 - Datafile is NetCDF format, tracking time-averaged solar eve on surface

Sourced from: [NASA Giovanni](https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=2019-01-01T00:00:00Z&endtime=2022-11-30T23:59:59Z&data=FLDAS_NOAH01_CP_GL_M_001_SWdown_f_tavg)

### Earthquakes
Datafile: [earthquakes.tsv](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/natural_disasters/earthquakes/earthquakes.tsv)

 - Data is for years 2012 to 2022
 - Only selected earthquakes with magnitude ≥ 6, as that is the start of severe building damage
 - Datafile is TSV format, each row is an occurrence

Sourced from: [NOAA](https://data.noaa.gov/metaview/page?xml=NOAA/NESDIS/NGDC/MGG/Hazards/iso/xml/G012153.xml&view=getDataView)

### Tsunamis
Datafile: [runups.tsv](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/natural_disasters/tsunamis/runups.tsv)

 - Data is for years 2012 to 2022
 - Only selected tsunamis that are "definite", which means there is documentable proof that it occurred
 - Datafile is TSV format, each row is an occurrence
 - Data does not display source of tsunamis but rather locations affected by tsunamis

Sourced from: [NOAA](https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/runup-data?sourceMaxYear=2022&sourceMinYear=2012&sourceMinEventValidity=4)

### Tropical Cyclones / Hurricanes
Datafile: [hurricanes.csv.zip](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/natural_disasters/hurricanes/hurricanes.csv.zip)

 - Data is for years 1980 to 2022
 - Only displayed data for years 2012 to 2022
 - Datafile is CSV format, each row is an occurrence
 - Datafile is zipped, unzip to view properly

Sourced from: [NOAA NCEI](https://www.ncei.noaa.gov/products/international-best-track-archive?name=rsmc-data)

## Map
See [here](https://bnidevs.github.io/datascience_team3_f22/) for most up-to-date visualization

(Visualization was originally a single picture but data overlays became too condensed and hard to see.)

Legend:
 - Green: population
 - Red X's: earthquakes
 - Blue X's: tsunamis
 - Teal lines: hurricanes
 - Blue pins: wind speed
 - Red pins: solar energy
Notes:
 - The box on the left side of the pin represents the location, and the "prick" on the right side of the pin represents the amount of energy. The longer the "prick", the higher the average energy.

## Installation
```
make venv
make install
```

## Execution
```
make -j10 runall
```

`-j` flag is optional for parallel execution, `10` signifies number of simultaneous threads

If sequential execution is preferred, use command written below instead
```
make runall
```