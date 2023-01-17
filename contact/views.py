from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
#for sending email
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.template import loader
from .models import *



# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'name': 'Sadiqul Islam'
    }
    return HttpResponse(template.render(context, request))


def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contact with us!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid email address.')


    context = {
        'form':form,
        }
    return render(request, 'contact/contact.html', context)


def contact_list(request):
    contact_list = Contact.objects.all().values()
    template = loader.get_template('contact/contact_list.html')
    return HttpResponse(template.render({'contact_list': contact_list}, request))

def usercreation(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            subject = 'Account is created'
            body = render_to_string('contact/send_email.html',{
                'user': user,
                'domain': current_site.domain,
            })
            # recipient = form.cleaned_data.get('email')
            email = EmailMessage(subject, body, to=['mdsadiqulislam446@gmail.com'])
            email.send()
            messages.success(request, 'Account is created successfully!')
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/create_account.html', {'form':form})
