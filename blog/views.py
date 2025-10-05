from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging 
from blog.models import Post
from django.http import Http404

#static demo data
# posts = [
#         {'id':1, 'title':'First Post', 'content':'This is the first post.'},
#         {'id':2, 'title':'Second Post', 'content':'This is the second post.'},
#         {'id':3, 'title':'Third Post', 'content':'This is the third post.'}
#     ]

# Create your views here.
def index(request):
    blog_title = "Latest Blog Posts"
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "blog/index.html", {"blog_title": blog_title, "posts":posts} )

def detail(request, slug):
    #getting post data from the static demo data
    #post = next((item for item in posts if item['id']==int(post_id)), None)

    # logger = logging.getLogger('TESTING')
    # logger.debug(f'post variable is {post}')

    #getting post data from database
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    return render(request, "blog/details.html", {"post":post})

def old_url_redirect(request):
    return redirect(reverse("blog:new-url"))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")