from django.shortcuts import render,HttpResponse,redirect
from MyHomeApp.models import Contact
from django.contrib import messages
from MyBlogApp.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    # logout(request)
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

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        
        if len(username)>15:
            messages.error(request,"Username must be under 15 characters")
            return redirect("/")
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers")
            return redirect("/")
        if password!=confirmpassword:
            messages.error(request,"Password do not match")
            return redirect("/")
        
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request,"Your Blog Account Has Been Successfully Created")
        return redirect("/")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
        else:
            messages.error(request,"Invallid Credentials, Please Try Again")
        return redirect("/")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect("/")