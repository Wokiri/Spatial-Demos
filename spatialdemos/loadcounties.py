# Auto-generated `LayerMapping` dictionary for Region model

import os
from django.contrib.gis.utils import LayerMapping
from .models import KenyaCounty

counties = os.path.join(os.getcwd(), 'spatialdemos', 'demoassets', 'KenyaCounties.shp')

# Auto-generated `LayerMapping` dictionary for NairobiConstituency model
kenyacounty_mapping = {
    'name': 'name',
    'geom': 'MULTIPOLYGON',
}

def run(verbose=True):
    layermap = LayerMapping(KenyaCounty, counties, kenyacounty_mapping, transform=False)
    layermap.save(strict=True, verbose=verbose)