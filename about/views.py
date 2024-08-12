from django.shortcuts import render
from about.models import About

# Create your views here.


def aboutView(request):
    about = About.objects.all()
    return render(request, 'landing/index.html', context={
        'about': about,
    })
