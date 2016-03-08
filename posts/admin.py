from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"]
	list_filter = ["updated","timestamp"]
	list_display_links = ["updated"] #if you want title to be editable then this is needed
	search_fields = ["title","content"] #add search box
	list_editable = ["title"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)

