from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Status(models.Model):
    user=models.OneToOneField(User, on_delete = models.CASCADE)
    name=models.CharField(max_length=75)
    USER_CHOICES = (
    ('Donor', 'Donor'),
    ('Recipient', 'Recipient'),
    ('Store', 'Store'),
    ('Helper', 'Helper')
    )
    type_user=models.CharField(max_length=20, choices = USER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Donor(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    donation_option_1=models.DecimalField(max_digits=6, decimal_places=2)
    donation_option_2=models.DecimalField(max_digits=6, decimal_places=2)
    donation_option_3=models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    


class Recipient(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    identifier=models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Store(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Helper(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    verified = models.BooleanField(default=False)  
    recipients = models.ForeignKey(Recipient, on_delete=models.PROTECT)
      