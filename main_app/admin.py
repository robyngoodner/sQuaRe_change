from django.contrib import admin
from .models import Status, Donor, Recipient, Store, Helper, Account, Transaction

# Register your models here.
admin.site.register(Status)
admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Store)
admin.site.register(Helper)
admin.site.register(Account)
admin.site.register(Transaction)