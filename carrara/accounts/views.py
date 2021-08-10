# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

'''
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
'''
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        ip_address=''
        # email = form('email',None)
        
        if form.is_valid():
            if request.user.is_authenticated:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is logged in :)"+ ip_address )
                print(f"Username --> {request.user.username}"+ ip_address)
            else:
                ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
                print("User is not logged in : "+ ip_address)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../../archivi/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})