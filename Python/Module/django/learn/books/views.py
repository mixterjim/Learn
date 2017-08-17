from django.shortcuts import render_to_response
from django.views.generic import DetailView, ListView
from books.models import Book, Publisher


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search.html', {'books': books, 'query': q})
    return render_to_response('books/search.html', {'errors': errors})


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers_list'
    # publisher_list.html:{% for publisher in publishers_list %}
    queryset = Publisher.objects.order_by('name')
    template_name = 'books/another.html'
