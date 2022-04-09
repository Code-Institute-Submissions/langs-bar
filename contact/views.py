from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contact(request):
    """
    A View to submit user contact forms
    for admin to view backend.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Website Contact Form"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                                            ['admin@example.com'])
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Form successfully processed!'
                             ' A team member will be in touch shortly')
            return redirect(contact)

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
