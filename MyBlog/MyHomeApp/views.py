from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def contact(request):
    return HttpResponse("contact Page")

def about(request):
    return HttpResponse("about Page")