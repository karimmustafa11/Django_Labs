from django.contrib import admin
from .models import Book, Category, ISBN

class ISBNInline(admin.StackedInline):
    model = ISBN
    extra = 0

class BookAdmin(admin.ModelAdmin):
    inlines = [ISBNInline]
    list_display = ('title', 'user')
    list_filter = ('categories',)

admin.site.register(Book, BookAdmin)
admin.site.register(Category)