from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Status(models.Model):
    name=models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    USER_CHOICES = (
    ('D', 'Donor'),
    ('R', 'Receiver'),
    ('S', 'Store'),
    ('H', 'Helper')
    )
    type_user=models.CharField(max_length=20, choices = USER_CHOICES)
    donation_options=models.JSONField()
    qr_code=models.CharField(max_length=500)
    identifier=models.CharField(max_length=50, unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

