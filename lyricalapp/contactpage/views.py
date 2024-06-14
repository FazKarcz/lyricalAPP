from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            EmailMessage(
               'Contact Form Submission from {}'.format(name),
               message,
               email, # mail z ktorego zostala wyslana wiadomosc 
               ['hmutest@op.pl'], # skrzynka na ktora przychodzi wiadomosc
               [],
               reply_to=[email] # Email z formularza aby mozna bylo sie skontakotwac
            ).send()

            return redirect('contactpage:contact')
    else:
        form = ContactForm()
    return render(request, 'contactpage/contact.html', {'form': form})
