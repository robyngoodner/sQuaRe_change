from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Status, Donor, Recipient, Store, Helper, Account, Transaction
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from random import randint


# add @method_decorator(login_required, name='dispatch') in the line before any views that you must be logged in in order to see
# Create your views here.
class Home(TemplateView):
    template_name="home.html"

@method_decorator(login_required, name='dispatch')
class Logged_Home(TemplateView):
    template_name='logged_home.html'

    def get(self, request, *args, **kwargs):
        status=Status.objects.filter(user=request.user)
        donors=Donor.objects.filter(user=request.user)
        recipients=Recipient.objects.filter(user=request.user)
        stores=Store.objects.filter(user=request.user)
        helpers=Helper.objects.filter(user=request.user)
        account=Account.objects.get(user=request.user)
        transactions=Transaction.objects.filter(accounts = account)
        random_recipient = Recipient.objects.order_by('?')[0]
        random_user = Status.objects.get(user=random_recipient.user)
        
        return render(request, self.template_name, {'status': status, 'donors': donors, 'recipient': recipients, 'store': stores, 'helper': helpers, 'account': account, 'transactions': transactions, 'random_user_name':random_user.name, "random_user_bio": random_recipient.bio})

class About(TemplateView):
    template_name="about.html"

class Register(CreateView):
    model = Status
    fields = ['name','type_user']
    template_name="register.html"
    user_type=''
    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        print(f'line 34{self.object.type_user}')
        self.object.save()
        print(f'line35{self}')
        user_type=self.object.type_user
        Account.objects.create(user=self.request.user)
        if user_type == 'Donor':
            return HttpResponseRedirect('/donor/new')
        elif user_type == 'Recipient':
            return HttpResponseRedirect(f'/recipient/{self.object.user}/new')
    if user_type == 'Donor':
        success_url="donor/new"
    elif user_type == "Recipient":
        success_url = "recipient/new"

# django auth
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/register/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
            form=UserCreationForm()
            return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    print('The account has been diabled.')
                    return render(request, 'login.html', {'form': form})
            else:
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form':form})
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

# @method_decorator(login_required, name='dispatch')
def profile(request, username):
    user=User.objects.get(username=username)
    status=Status.objects.filter(user=user)
    donors=Donor.objects.filter(user=user)
    recipients=Recipient.objects.filter(user=user)
    stores=Store.objects.filter(user=user)
    helpers=Helper.objects.filter(user=user)
    account=Account.objects.get(user=user)
    transactions=Transaction.objects.filter(accounts = account)
    random_recipient = Recipient.objects.order_by('?')[0]
    random_user = Status.objects.get(user=random_recipient.user)
    return render(request, 'profile.html', {'username': username, 'status': status, 'donors': donors, 'recipient': recipients, 'store': stores, 'helper': helpers, 'account': account, 'transactions': transactions, 'random_user_name':random_user.name, "random_user_bio": random_recipient.bio})

# def profile_update(request, username):
#     user=User.objects.get(username=username)
#     status=Status.objects.filter(user=user)
#     return render(request, 'profile_edit.html', {'user': user, 'status': status})


class Donor_Create(CreateView):
    model = Donor
    fields = ["donation_option_1", "donation_option_2", "donation_option_3"]
    template_name="user_create.html"
    def get_success_url(self):
        return reverse('user_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # print(f'line 100 {self.object}')
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/')
    success_url="/"

class Donor_Update(UpdateView):
    model = Donor
    fields = ["donation_option_1", "donation_option_2", "donation_option_3"]
    template_name="donor_update.html"
    def get_success_url(self):
        return reverse('home')

class Recipient_Form(forms.Form):
    identifier=forms.CharField(label="Please give yourself a unique identifier", max_length = 50)
    bio=forms.CharField(label="We believe that people are more likely to donate to those in need if they know a little bit about them. Would you be comfortable sharing your story? Donators will be able to see it when they donate to you, and it may show up as a 'highlighted story' for other users of the app.", max_length=500)

def recipient_create(request, username):
    if request.method == 'POST':
        form = Recipient_Form(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            Recipient.objects.create(user=User.objects.get(username=username),  identifier=identifier)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'user_create.html', {'form': form})
    else:
        form = Recipient_Form()
        return render(request, 'user_create.html', {'form': form})

@login_required
def payment(request, username):
    recipient=User.objects.get(username=username)
    print(request.user)
    donor=User.objects.get(username=request.user)
    donations=Donor.objects.get(user=request.user)
    
    return render(request, 'payment.html', {'recipient': recipient, "donor": donor, "donations": donations})

def payment_update(request, username, donation):
    recipient=User.objects.get(username=username)
    donor = User.objects.get(username=request.user)
    recipient_account = Account.objects.update_or_create(user=recipient, defaults={'value': 0})
    # recipient_account=Account.objects.get(user=recipient.pk)
    donor_account = Account.objects.update_or_create(user=donor, defaults={'value': 0})
    recipient_account = Account.objects.get(user=recipient)
    donor_account = Account.objects.get(user=donor)
    # donor_account=Account.objects.get(user=donor.pk)
    print("recipient",recipient_account.value)
    print("donation",donation)
    recipient_account.value = float(recipient_account.value) + float(donation)
    recipient_account.save(update_fields=['value'])
    donor_account.value = float(donor_account.value) - float(donation)
    donor_account.save(update_fields=['value'])
    transaction=Transaction(value=donation, donor=request.user, recipient=username)
    transaction.save()
    transaction.accounts.add(recipient_account, donor_account)
    
    status=Status.objects.filter(user=request.user)
    donors=Donor.objects.filter(user=request.user)
    recipients=Recipient.objects.filter(user=request.user)
    stores=Store.objects.filter(user=request.user)
    helpers=Helper.objects.filter(user=request.user)
    accounts=Account.objects.filter(user=request.user)
    # users=User.objects.all()
    return render(request, 'profile.html', {'username': username, 'status': status, 'donors': donors, 'recipient': recipients, 'store': stores, 'helper': helpers, 'accounts': accounts})

