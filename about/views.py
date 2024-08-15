from django.shortcuts import render
from about.models import About, Skill
from account.models import User  # Adjust the import based on your app structure
from django.contrib.auth import get_user_model
from contact.models import Contact
from photos.models import Photo
from services.models import Service
from teams.models import Team
from works.models import Work
from about.forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect





User = get_user_model()


def aboutView(request):
    user= User.objects.all() 
    about = About.objects.all()
    skill = Skill.objects.all()
    service = Service.objects.all()
    team = Team.objects.all()
    work = Work.objects.all()
    photo = Photo.objects.all()
    contact = Contact.objects.all()

    if request.method == "POST":
       
        form = ContactForm(request.POST)
        if form.is_valid():
            

            
            form.save(commit=False)
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            recipients = ["hasanab286.py@gmail.com"]
            subject = f"Contact Form {firstname} {lastname}"
           
            try:
                send_mail(
                    subject=subject,
                    message=f"Message: {message}\nname:{firstname} {lastname}\n From: {email}",
                    from_email=email,
                    recipient_list=recipients,
                    fail_silently=False,
                )
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

            
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect("/#contact-section")

    else:
        form = ContactForm()


    return render(request, 'landing/index.html', context={
        'user' : user,
        'about': about,
        'skill': skill,
        'service': service,
        'team': team,
        'work': work,
        'photo': photo,
        'contact': contact,
        'form': form,
    })
