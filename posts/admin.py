from django.contrib import admin

# Register your models here.
from .models import Post #new

admin.site.register(Post)
