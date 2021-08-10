from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


def sendMail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            #estrae da cd ... i dati scaricati da form.cleaned_data
            email = cd['recipient']
            subject = "Invio email da "+ email
            message = cd['message']
            message = message + " indirizzo email del mittente : " + email

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'mailer/index.html', {

        'form': form,
        'messageSent': messageSent,

    })