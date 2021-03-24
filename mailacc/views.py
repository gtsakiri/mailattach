from django.shortcuts import render
from .models import Mailbox
# Create your views here.
def mailbox_list(request):

    all_emails=Mailbox.objects.filter(active=1).order_by('name')

    context = {'all_emails': all_emails,
               }
    return render(request, 'mailacc/mailbox_list.html', context)