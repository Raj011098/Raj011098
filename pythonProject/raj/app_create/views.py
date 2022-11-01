from django.shortcuts import render
from . models import *
def home(request):
    return render(request,"home.html")
def Insertdata (request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    Email = request.POST['email']
    contact = request.POST['contact']
    print(firstname)
    print(lastname)
    print(Email)
    print(contact)
    newuser = ether.objects.create(
        firstname=firstname,lastname=lastname,email=Email,contact=contact)
    return render(request, 'show.html')

def value(request):
    return render(request,"valueerror page.html")


