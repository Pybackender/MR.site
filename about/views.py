from django.shortcuts import render
from about.models import About
from account.models import User  # Adjust the import based on your app structure
from django.contrib.auth import get_user_model

from services.models import Service


# Create your views here.
User = get_user_model()


def aboutView(request):
    user= User.objects.all() 
    about = About.objects.all()
    service = Service.objects.all()

    return render(request, 'landing/index.html', context={
        'user' : user,
        'about': about,
        'service': service,
    })
