from django.db import models
from django.utils import timezone

class Mailbox(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    maildir = models.CharField(max_length=255)
    quota = models.BigIntegerField()
    local_part = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mailbox'

    def __str__(self):
        return self.username