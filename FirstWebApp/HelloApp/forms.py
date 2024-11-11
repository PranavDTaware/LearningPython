from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)


class RegistrationFrom(forms.Form):
    email = forms.EmailField()
    contactnumber = forms.CharField(max_length=10)
    fisrtname = forms.CharField(max_length=100)
    lastname= forms.CharField(max_length=100)
    location= forms.CharField(max_length=100)