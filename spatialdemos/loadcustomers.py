# Auto-generated `LayerMapping` dictionary for Region model

import os
from django.contrib.gis.utils import LayerMapping
from .models import StoreCustomer

customers = os.path.join(os.getcwd(), 'spatialdemos', 'demoassets', 'RetailStoreCustomers.shp')

# Auto-generated `LayerMapping` dictionary for NairobiConstituency model
storecustomer_mapping = {
    'name': 'Name',
    'geom': 'MULTIPOINT',
}

def run(verbose=True):
    layermap = LayerMapping(StoreCustomer, customers, storecustomer_mapping, transform=False)
    layermap.save(strict=True, verbose=verbose)