from django.shortcuts import render_to_response, get_object_or_404
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
    context_object_name = 'publishers_list'  # Default: object_list
    queryset = Publisher.objects.order_by('name')
    template_name = 'books/another.html'  # [publisher_list.html,another.html]


class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        context = super(PublisherBookList, self).get_context_data(**kwargs)
        # Call the base implementation first to get a context
        context['publisher'] = self.publisher
        # Add in the publisher
        return context
