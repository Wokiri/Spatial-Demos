from django.shortcuts import render
from contents.models import Service
from contents.forms import InquiryForm

# Create your views here.
def homeView(request):

    pageName = 'Home'
    services = Service.ready.all()
    inquiry_form = InquiryForm()

    context = {
        'pageName': pageName,
        'services': services,
        'inquiry_form': inquiry_form
    }

    return render(request, 'pages/home.html', context)


# Create your views here.
def projectsView(request):

    pageName = 'Projects'

    context = {
        'pageName': pageName,
    }

    return render(request, 'pages/projects.html', context)


# Create your views here.
def articlesView(request):

    pageName = 'Articles'

    context = {
        'pageName': pageName,
    }

    return render(request, 'pages/articles.html', context)