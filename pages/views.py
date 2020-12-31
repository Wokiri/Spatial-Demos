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
