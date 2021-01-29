# Auto-generated `LayerMapping` dictionary for Region model

import os
from django.contrib.gis.utils import LayerMapping
from .models import CountriesZones

countries = os.path.join(os.getcwd(), 'maps', 'mapassets', 'countrieszones.shp')

# Auto-generated `LayerMapping` dictionary for CountriesZones model
countrieszones_mapping = {
    'name': 'name',
    'iso': 'iso',
    'zone': 'zone',
    'colormap': 'colormap',
    'geom': 'MULTIPOLYGON',
}

def run(verbose=True):
    layermap = LayerMapping(CountriesZones, countries, countrieszones_mapping, transform=False)
    layermap.save(strict=True, verbose=verbose)