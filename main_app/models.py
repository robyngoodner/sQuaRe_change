from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Status(models.Model):
    name=models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    USER_CHOICES = (
    ('Donor', 'Donor'),
    ('Receiver', 'Receiver'),
    ('Store', 'Store'),
    ('Helper', 'Helper')
    )
    type_user=models.CharField(max_length=20, choices = USER_CHOICES)
    donation_option_1=models.DecimalField(max_digits=6, decimal_places=2)
    donation_option_2=models.DecimalField(max_digits=6, decimal_places=2)
    donation_option_3=models.DecimalField(max_digits=6, decimal_places=2)
    qr_code=models.CharField(max_length=500)
    identifier=models.CharField(max_length=50, unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

