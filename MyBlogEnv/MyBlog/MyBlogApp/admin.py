from django.contrib import admin
from MyBlogApp.models import Post,BlogComment
# Register your models here.
admin.site.register((BlogComment))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyMCE.js',)