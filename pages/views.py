from django.shortcuts import render
from contents.models import Service

# Create your views here.
def homeView(request):

    pageName = 'Home'
    services = Service.ready.all()

    context = {
        'pageName': pageName,
        'services': services
    }

    return render(request, 'pages/home.html', context)
