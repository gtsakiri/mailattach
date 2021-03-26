from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from mailattach import settings
from .models import Mailbox
from django.core.mail import EmailMessage

# Create your views here.
def mailbox_list(request):

    all_emails=Mailbox.objects.filter(active=1).order_by('name')

    context = {'all_emails': all_emails,
               }
    return render(request, 'mailacc/mailbox_list.html', context)

def sendMessage(request):
    if request.method=='POST':
        paramsubject = request.POST.get('msgtitle')
        paramtext = request.POST.get('msgtext')
        paramreceivers = request.POST.get('multiReceivers')
        attachlist = request.FILES.get('customfile')


        subject = paramsubject
        message = paramtext
        email_from = settings.EMAIL_HOST_USER
        recipient_list = paramreceivers.split(",")
        if  paramreceivers:
            mail=EmailMessage(subject, message, email_from, recipient_list)
            mail.attach(attachlist.name, attachlist.read(), attachlist.content_type)
            mail.send()
            context={'msg':attachlist}
        else:
            context = {'msg':'No recipients!',}


    return render(request, 'mailacc/Sendresult.html',context)