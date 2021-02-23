# Auto-generated `LayerMapping` dictionary for Region model

import os
from django.contrib.gis.utils import LayerMapping
from .models import NairobiConstituency

constituencies = os.path.join(os.getcwd(), 'spatialdemos', 'demoassets', 'NairobiConstituencies.shp')

# Auto-generated `LayerMapping` dictionary for NairobiConstituency model
nairobiconstituency_mapping = {
    'name': 'Name',
    'geom': 'MULTIPOLYGON',
}

def run(verbose=True):
    layermap = LayerMapping(NairobiConstituency, constituencies, nairobiconstituency_mapping, transform=False)
    layermap.save(strict=True, verbose=verbose)