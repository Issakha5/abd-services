from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'subject': form.cleaned_data['subject'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                          ['issakhad5@gmail.com','issakha.dev@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")

    form = ContactForm()
    return render(request, "base.html", {'form': form})


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                 'name': form.cleaned_data['name'],
#                 'subject': form.cleaned_data['subject'],
#                 'email': form.cleaned_data['email'],
#                 'message': form.cleaned_data['message'],
#             }
#             message = "\n".join(body.values())
#
#             try:
#                 send_mail(subject, message, settings.EMAIL_HOST_USER,
#                           ['issakhad5@gmail.com','issakha.dev@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect("/")
#
#     form = ContactForm()
#     return render(request, "contactus_section.html", {'form': form})

