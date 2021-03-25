from django.shortcuts import render

from mailattach import settings
from .models import Mailbox
from django.core.mail import send_mail

# Create your views here.
def mailbox_list(request):

    all_emails=Mailbox.objects.filter(active=1).order_by('name')

    context = {'all_emails': all_emails,
               }
    return render(request, 'mailacc/mailbox_list.html', context)

def sendMessage(request):
    paramsubject = request.GET.get('msgtitle')
    paramtext = request.GET.get('msgtext')
    paramreceivers = request.GET.get('multiReceivers')

    subject = paramsubject
    message = paramtext
    email_from = settings.EMAIL_HOST_USER
    recipient_list = paramreceivers.split(",")
    send_mail(subject, message, email_from, recipient_list)

    return render(request, 'mailacc/Sendresult.html')