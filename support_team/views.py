from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SupportUserRegisterForm
from django.contrib.auth.models import Group


def register(request):
    if request.method == "POST":
        form = SupportUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            support_group = Group.objects.get(name='support_team')
            support_group.user_set.add(user)

            username = form.cleaned_data.get('username')
            messages.success(request, f'User account created: {username}, you can login now')
            return redirect('login')
    else:
        form = SupportUserRegisterForm()
    return render(request, 'support_team/register_user.html', {'form': form})
