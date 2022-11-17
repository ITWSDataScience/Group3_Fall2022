from PIL import Image
from population_count.population import population 
from natural_disasters.earthquakes.earthquakes import earthquakes
from energy_strength.wind.wind import wind

img = Image.new('RGB', [8640, 4320], 0) # ascii data is 8640 by 4320
pixel_map = img.load() # load pixel map for image

population(pixel_map)
earthquakes(pixel_map)
wind(pixel_map)

img.save('map.png')