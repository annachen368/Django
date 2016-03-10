from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

def posts_create(request):

	return HttpResponse("<h1>posts_create<h1>")

def posts_detail(request):
	context = {
		"title":"detail"
	}
		
	return render(request,"index.html",context)

def posts_list(request):
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title":"My User List"
	# 	}
	# else:
	# 	context = {
	# 		"title":"List"
	# 	}

	queryset = Post.objects.all()
	context = {
		"obj_list":queryset,
		"title":"List"
	}

	return render(request,"index.html",context)

def posts_update(request):

	return HttpResponse("<h1>posts_update<h1>")

def posts_delete(request):

	return HttpResponse("<h1>posts_delete<h1>")
