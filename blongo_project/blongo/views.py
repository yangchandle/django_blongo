from django.shortcuts import render
from django.http import HttpResponse
from blongo.models import Post
from django.template import Context, loader

def index(request):
	latest_posts = Post.objects
	t = loader.get_template('index.html')
	context_dict = {'latest_posts': latest_posts}
	c = Context(context_dict)
	return HttpResponse(t.render(c))

# Create your views here.
