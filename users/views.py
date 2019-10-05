from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.utils  import translation
user_language = 'fi'

def register(request):
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for %s'%username)
            return redirect('Blog-Home')
    else :
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})
