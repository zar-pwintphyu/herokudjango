from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.conf import settings
from django.contrib.auth.models import Group, User
from .forms import SignUpForm





def signupView(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


