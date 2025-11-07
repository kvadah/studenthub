from django.contrib import admin

# Register your models here.
from .models import Student, Post, Comment, Reply
admin.site.register(Student)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Comment)
