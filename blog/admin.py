from django.contrib import admin
from .models import AuthorsProfileInfo, BlogPost, BlogComment

admin.site.register(AuthorsProfileInfo)
admin.site.register(BlogPost)
admin.site.register(BlogComment)
