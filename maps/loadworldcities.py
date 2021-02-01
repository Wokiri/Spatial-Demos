# Auto-generated `LayerMapping` dictionary for Region model

import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldCities

countries = os.path.join(os.getcwd(), 'maps', 'mapassets', 'WorldCities.shp')

# Auto-generated `LayerMapping` dictionary for CountriesZones model
worldcities_mapping = {
    'city': 'city',
    'country': 'country',
    'region': 'region',
    'accentcity': 'accentcity',
    'geom': 'POINT',
}

def run(verbose=True):
    layermap = LayerMapping(WorldCities, countries, worldcities_mapping, transform=False)
    layermap.save(strict=True, verbose=verbose)