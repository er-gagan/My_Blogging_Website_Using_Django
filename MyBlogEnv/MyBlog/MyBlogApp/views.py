from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from MyBlogApp.models import Post,BlogComment
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,"blog/blogHome.html",context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(BlogPost=post)
    context = {'post':post,'comments':comments}
    return render(request,"blog/blogPost.html",context)

def postComment(request):
    if request.method=='POST':
        comment = request.POST.get("comment")
        User = request.user
        Post_S_No = request.POST["postSno"]
        BlogPost = Post.objects.get(S_No=Post_S_No)
        BlogComment(comment=comment, User=User, BlogPost=BlogPost).save()
        messages.success(request,"Your comment has been posted successfully")
    return redirect(f"/blog/{BlogPost.slug}")