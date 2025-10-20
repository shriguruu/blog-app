from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging 
from blog.models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

#static demo data
# posts = [
#         {'id':1, 'title':'First Post', 'content':'This is the first post.'},
#         {'id':2, 'title':'Second Post', 'content':'This is the second post.'},
#         {'id':3, 'title':'Third Post', 'content':'This is the third post.'}
#     ]

# Create your views here.
def index(request):
    blog_title = "Latest Blog Posts"
    all_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/index.html", {"blog_title": blog_title, "page_obj":page_obj} )


def detail(request, slug):
    #getting post data from the static demo data
    #post = next((item for item in posts if item['id']==int(post_id)), None)

    # logger = logging.getLogger('TESTING')
    # logger.debug(f'post variable is {post}')

    #getting post data from database
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    return render(request, "blog/details.html", {"post":post, "related_posts":related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new-url"))

def new_url_view(request):
    return HttpResponse("This is the new URL view.")

def contact_view(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger('TESTING')
        if form.is_valid():
            logger.debug(f'POST data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message = 'Your email has been successfully sent'

            return render(request, "blog/contact.html", {'form':form, 'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request, "blog/contact.html", {'form':form, 'name':name, 'email':email, 'message':message})
    
            
    return render(request, "blog/contact.html")