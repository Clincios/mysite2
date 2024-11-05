from django.contrib import admin
from .models import Post
from .models import Contact
from .models import Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','updated_on','author','image_url','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','body','created_on')

admin.site.register(Post,PostAdmin)

admin.site.register(Comment,CommentAdmin)
admin.site.register(Contact)