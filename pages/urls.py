from django.urls import path
from .views import (
    homeView,
    projectsView,
    articlesView,
    submissionView,
    worldtimeView,
    country_detail
    )

app_name = 'pages'

urlpatterns = [
    path('', homeView, name='home_page'),
    path('status/', submissionView, name='submission_page'),
    path('projects/', projectsView, name='projects_page'),
    path('articles/', articlesView, name='articles_page'),
    path('worldtime/', worldtimeView, name='worldtime_page'),
    path('country/<int:country_id>', country_detail, name='countrydetail_page'),
]