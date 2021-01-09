from django.shortcuts import redirect, render
from contents.models import Service
from contents.forms import InquiryForm

from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

# Create your views here.
def homeView(request):

    pageName = 'Home'
    services = Service.ready.all()
    inquiry_form = InquiryForm()

    if request.method == 'POST':
        # Form was submitted
        inquiry_form = InquiryForm(request.POST)
        if inquiry_form.is_valid():
            # Form fields passed validation
            clean_client_data = inquiry_form.cleaned_data
            subject = f"Project Inquiry from {clean_client_data['client_name']}: {clean_client_data['client_email']}"
            message = f"Inquiry message: {clean_client_data['client_message']}\n\n"
            EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['wokirijoe@gmail.com']
            )
            messages.success(request, f"Hey {clean_client_data['client_name']}, your Inquiry is Successfully Sent.")
            inquiry_form = InquiryForm()
            return redirect('pages:submission_page')

    context = {
        'pageName': pageName,
        'services': services,
        'inquiry_form': inquiry_form
    }

    return render(request, 'pages/home.html', context)


# Create your views here.

def submissionView(request):

    pageName = 'Status'

    context = {
        'pageName': pageName,
    }

    return render(request, 'pages/submission.html', context)


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