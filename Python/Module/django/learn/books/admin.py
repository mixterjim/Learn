from django.contrib import admin
from books.models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)  # filter on left
    date_hierarchy = 'publication_date'  # filter on top
    ordering = ('-publication_date',)  # sort
    fields = ('title', 'authors', 'publisher', 'publication_date')  # order and only in the list can be seen
    filter_horizontal = ('authors',)  # when the option more than ten to use this(filter_vertical)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
