from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.serializers import serialize

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.gdal import OGRGeometry


from .models import (
    Customer,
    RetailStore,
    NairobiConstituency,
    StoreCustomer,
    SampledIssue,
    KenyaCounty,
    )

all_customers = StoreCustomer.objects.all()


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

    return render(request, 'spatialdemos/database_submissions.html', context)


def customer_distance_view(request):
    from .forms import DistanceValue

    pageName = 'Stores Map Demo'
    retail_store = get_object_or_404(RetailStore, id=1)
    store_customers = Customer.objects.all()
    
    dist_customers = []
    dist_input = DistanceValue(request.GET)
    querry_value = ''
    if dist_input.is_valid():
        cd = dist_input.cleaned_data
        querry_value = cd['distance_value']
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

    return render(request, 'spatialdemos/store_customerdistance.html', context)


def customer_location_view(request):

    pageName = 'Customer Location'
    nairobi_constituencies_json = serialize('geojson', NairobiConstituency.objects.all())
    all_customers_json = serialize('geojson', all_customers)

    context = {
        'pageName': pageName,
        'nairobi_constituencies_json': nairobi_constituencies_json,
        'all_customers_json': all_customers_json
    }

    return render(request, 'spatialdemos/store_customerlocation.html', context)


def customers_in_constituency_view(request, id):

    constituency = get_object_or_404(NairobiConstituency, id=id)
    customers_in_constituency = []
    pageName = f'{constituency} Constituency'

    constituency_ogr = OGRGeometry(constituency.geom.wkt)

    for customer in all_customers:
        customer_ogr = OGRGeometry(customer.geom.wkt)
        if constituency_ogr.contains(customer_ogr):
            customers_in_constituency.append(customer)
    

    context = {
        'pageName': pageName,
        'constituency': constituency,
        'customers_in_constituency': customers_in_constituency,
        'num_customers_in_constituency': len(customers_in_constituency),
    }

    return render(request, 'spatialdemos/customerconstituency.html', context)


def issues_list_view(request):

    pageName = 'Issues'

    context = {
        'pageName': pageName,
        'issues': SampledIssue.objects.all(),
    }

    return render(request, 'spatialdemos/issues.html', context)


def issue_detail_view(request, id):

    issue = get_object_or_404(SampledIssue, id=id)
    counties = issue.counties.all()
    pageName = f'{id} {issue.issue}'

    context = {
        'pageName': pageName,
        'issue': issue,
        'counties': counties,
        'counties_count': counties.count(),
        'counties_json': serialize('geojson', counties),
    }

    return render(request, 'spatialdemos/issue.html', context)
