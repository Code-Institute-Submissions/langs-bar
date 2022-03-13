from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .forms import EveningTables

# Create your views here.


def evening_table_form(request):
    """ A View to submit tables form """
    if request.method == 'POST':
        form = EveningTables(request.POST)
        if form.is_valid():
            form.save()
            subject = "Evening Table Enquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'guests': str(form.cleaned_data['guests']),
                'datetime': str(form.cleaned_data['datetime']),
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                                            ['admin@example.com'])
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Form successfully processed!' +
                             ' A team member will be in touch shortly')
            return redirect(evening_table_form)

    form = EveningTables()
    return render(request, "tables/booking.html", {'form': form})
