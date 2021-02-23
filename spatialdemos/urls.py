from django.urls import path

from .views import (
    home_view,
    forms_view,
    store_view,
    )

app_name = 'spatialdemos'

urlpatterns = [
    path('', home_view, name='homedemo_page'),
    path('forms/', forms_view, name='forms_page'),
    path('store/', store_view, name='storedemo_page'),

]
