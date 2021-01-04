from django.urls import path
from .views import homeView, projectsView, articlesView

app_name = 'pages'

urlpatterns = [
    path('', homeView, name='home_page'),
    path('projects/', projectsView, name='projects_page'),
    path('articles/', articlesView, name='articles_page'),
]