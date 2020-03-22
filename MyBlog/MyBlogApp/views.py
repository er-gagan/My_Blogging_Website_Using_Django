from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("This is BlogHome")

def blogPost(request,slug):
    return HttpResponse(f'This is BlogPost: {slug}')