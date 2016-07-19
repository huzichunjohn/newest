from django.contrib import admin
from .models import Blog, Author

class BlogAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
