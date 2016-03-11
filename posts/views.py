from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from .models import Post
from .forms import PostForm

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
		
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title":instance.title,
		"instance":instance,
	}
		
	return render(request,"post_detail.html",context)

def post_list(request):
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

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)

def post_delete(request):

	return HttpResponse("<h1>posts_delete<h1>")
