from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Status
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# add @method_decorator(login_required, name='dispatch') in the line before any views that you must be logged in in order to see
# Create your views here.

class Home(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name="about.html"

class Register(CreateView):
    model = Status
    fields = ['name','type_user', 'donation_option_1','donation_option_2','donation_option_3','qr_code','identifier']
    template_name="register.html"
    # def get_success_url(self):
    #     return reverse('user_detail', kwargs={'pk': self.object.pk})
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.userself.object.save()
    #     return HttpResponseRedirect('/home')
    success_url="/"

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
    return HttpResponseRedirect('/home')

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
                    return HttpResponseRedirect('/user/'+u)
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
    return render(request, 'profile.html', {'username': username, 'status': status})