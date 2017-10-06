from django.contrib import admin

from models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'image',
        'caption',
        'likes'
    )
    list_filter = (
        'id',
        'owner',
        'caption',
        'likes'
    )

admin.site.register(Post,PostAdmin)
