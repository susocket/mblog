from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from django.template.loader import get_template
from .models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    template = get_template('index.html')

    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    now = datetime.now()
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
