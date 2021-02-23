from django.contrib.gis import forms
from .models import (
    Customer,
    )

from django.core.validators import MinValueValidator

class CustomerForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Customer name',
            }
        )
    )

    location = forms.PointField(widget= forms.OSMWidget(
        attrs={
            'map_width': 927,
            'map_height': 500,
            'default_lat': -1.2921,
            'default_lon': 36.8219,
            'default_zoom': 18
            }
        ))

    class Meta:
        model = Customer
        fields = ['name', 'fav_food', 'location']


class DistanceValue(forms.Form):
    distance_value = forms.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])