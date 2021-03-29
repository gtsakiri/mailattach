from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from mailattach import settings
from .models import Mailbox
from django.core.mail import EmailMessage

# Create your views here.
def mailbox_list(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    all_emails=Mailbox.objects.filter(active=1).order_by('name')

    context = {'all_emails': all_emails,
               }
    return render(request, 'mailacc/mailbox_list.html', context)

def sendMessage(request):

    if request.method=='POST':
        paramsubject = request.POST.get('msgtitle')
        paramtext = request.POST.get('msgtext')
        paramreceivers = request.POST.get('multiReceivers')
        parambcc = request.POST.get('multiBcc')
        attachlist = request.FILES.getlist('customfile')  #λίστα συνημμένων

        subject = paramsubject
        message = paramtext
        email_from = settings.EMAIL_HOST_USER
        recipient_list = paramreceivers.split(",")
        bcc_list = parambcc.split(",")
        if  paramreceivers or parambcc:  #αν υπάρχουν παραλήπτες...
            mail=EmailMessage(subject, message, email_from, recipient_list,bcc_list)
            for file_to_attach in attachlist:   #κάθε συνημμένο φορτώνεται
                mail.attach(file_to_attach.name, file_to_attach.read(), file_to_attach.content_type)
            mail.send()
            context={'msg':'Mail sent!'}
        else:     #αλλιώς σφάλμα...
            context = {'msg':'No recipients!',}


    return render(request, 'mailacc/Sendresult.html',context)