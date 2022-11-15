# Data Science Fall 2022
### Group 3 - Los Pollos Hermanos
Dean Vogel, Julian Lioanag, Nathan Agpalo, Bill Ni

Optimal placement of renewable energy sources (wind, solar, geothermal) based on energy strength, energy consumption, distance to populated areas, crime rate, natural disaster frequency, and other notable factors.

## Data Sources
### Population
Datafile: [gpw_pop.asc](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/population_count/gpw_pop.asc.zip)

 - Data is for 2020 values
 - Datafile is zipped, unzip to view properly

Sourced from: [NASA SEDAC](https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-count-rev11)

### Earthquakes
Datafile: [earthquakes.tsv](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/natural_disasters/earthquakes/earthquakes.tsv)

 - Data is for years 2012 to 2022
 - Only selected earthquakes with magnitude ≥ 6, as that is the start of severe building damage

Sourced from: [NOAA](https://data.noaa.gov/metaview/page?xml=NOAA/NESDIS/NGDC/MGG/Hazards/iso/xml/G012153.xml&view=getDataView)

## Map
This is the most up-to-date map with all datasets included:

![map](https://github.com/ITWSDataScience/Group3_Fall2022/blob/main/map.png)

Legend:
 - Green: population
 - Red X's: earthquakes

## Installation
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Execution
```
python3 main.py
```