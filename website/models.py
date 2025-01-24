from django.db import models
from accounts.validators import validate_iranian_cellphone_number

class ContactUsModel(models.Model):
    subject = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_cellphone_number],null=True,blank=True)
    content = models.TextField()
    seen = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    def full_name(self):
        return self.first_name + " " + self.last_name

class NewsletterModel(models.Model):
    email = models.EmailField()
    seen = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email