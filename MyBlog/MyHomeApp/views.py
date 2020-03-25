from django.shortcuts import render,HttpResponse
from MyHomeApp.models import Contact
from django.contrib import messages
from MyBlogApp.models import Post

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

def search(request):
    query = request.GET['query']
    if len(query)>80:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(Title__icontains=query)
        allPostContent = Post.objects.filter(Content__icontains=query)
        allPosts = allPostsTitle.union(allPostContent)
    if allPosts.count() == 0:
        messages.warning(request,"No Search Result Found, Please Refine Your Query")
    context = {'allPosts':allPosts,'query':query}
    return render(request,"home/search.html",context)