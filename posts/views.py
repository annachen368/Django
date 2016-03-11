from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from .forms import PostForm

def posts_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
		# raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		# messages.success(request, "Successfully Created")
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def posts_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title":instance.title,
		"instance":instance,
	}
		
	return render(request,"post_detail.html",context)

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
