from django.contrib.gis import forms
from maps.models import UserPoint, UserPolygon


# class LocationForm(forms.ModelForm):

#     location = forms.PointField(widget= forms.OpenLayersWidget(
#         attrs={
#             'map_width':600,
#             'map_height':500,
#             }
#         ))

#     class Meta:
#         model = UserPoint
#         fields = ['name', 'location']

class LocationForm(forms.ModelForm):

    location = forms.PointField(widget= forms.OSMWidget(
        attrs={
            'map_width':600,
            'map_height':500,
            'default_lat': -1.2921,
            'default_lon': 36.8219,
            'default_zoom': 15
            }
        ))

    class Meta:
        model = UserPoint
        fields = ['name', 'location']

# class LocationForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     location = forms.PointField(widget= forms.OpenLayersWidget(
#         attrs={
#             'map_width':600,
#             'map_height':500,
#             'default_lat': -1.8,
#             'default_lon': 36.4,
#             'default_zoom': 8
#             }
#         ))


class UserPolygonForm(forms.ModelForm):

    location = forms.PolygonField(widget= forms.OSMWidget(
        attrs={
            'map_width':600,
            'map_height':500,
            'default_lat': -1.2921,
            'default_lon': 36.8219,
            'default_zoom': 15
            }
        ))

    class Meta:
        model = UserPolygon
        fields = ['name', 'location']