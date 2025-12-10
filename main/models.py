# main/models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    service = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BugReport(models.Model):
    name = models.CharField( max_length=200 )
    email = models.EmailField()
    bug_type= models.CharField(max_length=50)
    page_url= models.CharField(max_length=300, blank=True , null=True)
    description = models.TextField()
    date_submitted = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return self.name