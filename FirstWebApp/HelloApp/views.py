from django.shortcuts import render
from .forms import LoginForm, RegistrationFrom

# Create your views here.
from django.http import HttpResponse

def home(request):
     return HttpResponse("Welcome")
    # return render(request, 'HelloApp/templates/home.html')

def about(request):
     return HttpResponse("Transflower Learning Pvt. Ltd.")

def contact(request):
     return HttpResponse("call us : 5464651658")

def login(request):
     if request.method == 'POST':
          form = LoginForm(request.POST)
          if form.is_valid():
               # Process the data (e.g., save it to the database or send an email)
               email = form.cleaned_data['email']
               password = form.cleaned_data['password']
               # For now, just render a success message
               return render(request, 'HelloApp/home/home.html',{'email':email, 'password':password})
          else:
               form = LoginForm()
               return render(request, 'HelloApp/auth/login.html', {'form': form})
          
def register(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            # Process the data (e.g., save it to the database or send an email)
            email = form.cleaned_data['email']
            contactnumber = form.cleaned_data['contactnumber']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            location = form.cleaned_data['location']
           
            # For now, just render a success message
            return render(request, 'HelloApp/home/home.html',  
               {
                 'password': 'oooo', 
                 'email': email, 
                 'contactnumber': contactnumber, 
                 'firstname':firstname, 
                 'lastname':lastname, 
                 'location':location
               })
    else:
        form = RegistrationFrom()
    return render(request, 'HelloApp/auth/register.html', {'form': form})