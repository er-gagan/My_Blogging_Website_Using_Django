from django.shortcuts import render,HttpResponse
from MyHomeApp.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home/home.html")

def contact(request):
    if request.method == 'POST':
        Name = request.POST["Name"]
        Email = request.POST["Email"]
        Phone = request.POST["Phone"]
        Content = request.POST["Content"]
        Contact(Name=Name,Email=Email,Phone=Phone,Content=Content).save()
        messages.success(request,"Your Query Successfully Recorded")
    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")