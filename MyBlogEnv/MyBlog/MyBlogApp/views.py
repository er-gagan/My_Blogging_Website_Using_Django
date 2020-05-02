from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from MyBlogApp.models import Post,BlogComment
from MyBlogApp.templatetags import extras
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,"blog/blogHome.html",context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(BlogPost=post,Parent=None)
    replies = BlogComment.objects.filter(BlogPost=post).exclude(Parent=None)
    replyDict = {}
    for reply in replies:
        if reply.Parent.S_No not in replyDict.keys():
            replyDict[reply.Parent.S_No] = [reply]
        else:
            replyDict[reply.Parent.S_No].append(reply)
    context = {'post':post,'comments':comments,'user':request.user,'replyDict':replyDict}
    return render(request,"blog/blogPost.html",context)

def postComment(request):
    if request.method=='POST':
        comment = request.POST.get("comment")
        User = request.user
        Post_S_No = request.POST["postSno"]
        BlogPost = Post.objects.get(S_No=Post_S_No)
        
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment=comment, User=User, BlogPost=BlogPost)
            comment.save()
            messages.success(request,"Your comment has been posted successfully")
        else:
            Parent = BlogComment.objects.get(S_No=parentSno)
            comment = BlogComment(comment=comment, User=User, BlogPost=BlogPost, Parent=Parent)
            comment.save()
            messages.success(request,"Your reply has been posted successfully")
            
    return redirect(f"/blog/{BlogPost.slug}")