from django import forms
from about.models import About
from contact.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['firstname', 'email', 'lastname', 'message']  # Listt

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First name'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message', 'cols': '30', 'rows': '10'})    


    # def clean_name(self):
    #     data = self.cleaned_data.get('firstname')
    #     if len(data) < 1:
    #         raise forms.ValidationError("طول متن نباید کمتر از ۵ حرف باشد")
    #     return data

