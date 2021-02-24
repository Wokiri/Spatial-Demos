from django.urls import path

from .views import (
    home_view,
    forms_view,
    customer_distance_view,
    customer_location_view,
    customers_in_constituency_view,
    issues_list_view,
    issue_detail_view,
    coordinate_conversion_view,
    )

app_name = 'spatialdemos'

urlpatterns = [
    path('', home_view, name='homedemo_page'),
    path('forms/', forms_view, name='forms_page'),
    path('customerdistance/', customer_distance_view, name='customer_distance_page'),
    path('customerlocation/', customer_location_view, name='customer_location_page'),
    path('constituency/<int:id>', customers_in_constituency_view, name='customers_in_constituency_page'),
    path('governance/', issues_list_view, name='governance_mapping_page'),
    path('issue/<int:id>/', issue_detail_view, name='issue_page'),
    path('conversion/', coordinate_conversion_view, name='coordinate_conversion_page'),


]
