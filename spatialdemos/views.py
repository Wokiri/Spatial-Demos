
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

from django.contrib.gis.db.models.functions import Distance


from .models import RetailStore
from .models import Customer

# wgs_utm = CoordTransform(SpatialReference('WGS84'), SpatialReference('NAD83'))


def home_view(request):

    pageName = 'Home Demo'

    context = {
        'pageName': pageName,
    }

    return render(request, 'spatialdemos/home.html', context)


def forms_view(request):
    from .forms import CustomerForm

    pageName = 'Form Submissions'
    customer_map_form = CustomerForm()


    if request.method == 'POST':
        print('This is a POST')
        customer_map_form = CustomerForm(request.POST)
        if customer_map_form.is_valid():
            customer_map_form.save()
            clean_customer_data = customer_map_form.cleaned_data
            messages.success(request, f"{clean_customer_data['name']} has been successfully added into the database.")
            customer_map_form = CustomerForm()

    context = {
        'pageName': pageName,
        'customer_map_form': customer_map_form,
    }

    return render(request, 'spatialdemos/submissions.html', context)


def store_view(request):
    from .forms import DistanceValue

    pageName = 'Stores Map Demo'
    retail_store = get_object_or_404(RetailStore, id=1)
    store_customers = Customer.objects.all()
    
    dist_input = DistanceValue(request.GET)
    querry_value = request.GET.get('distance_value')

    if querry_value:
        querry_value = float(querry_value)
    else:
        querry_value = 50
    

    dist_customers = []
    for customer in Customer.objects.annotate(distance=Distance('location', retail_store.location)):
        if customer.distance.km >= querry_value:
            dist_customers.append(f'{customer.name} → {round(customer.distance.km, 2)} KM')
    
    context = {
        'pageName': pageName,
        'retail_store': retail_store,
        'store_customers': store_customers,
        'dist_customers': dist_customers,
        'dist_input': dist_input,
        'querry_value': querry_value
    }

    return render(request, 'spatialdemos/stores.html', context)
