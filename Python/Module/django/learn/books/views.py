from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView
from books.models import Book, Publisher
from io import BytesIO
from reportlab.pdfgen import canvas
import csv


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


def books_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=book.csv'
    # Create the HttpResponse object with the appropriate CSV header.
    writer = csv.writer(response)
    # Create the CSV writer using the HttpResponse as the "file."
    writer.writerow(['Id', 'Book', 'Publisher'])
    booklist = Book.objects.all()
    for (id, book) in zip(range(len(booklist)), booklist):
        publisher = book.publisher
        writer.writerow([id + 1, str(book), str(publisher)])

    return response


def books_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=book.pdf'
    # Create the HttpResponse object with the appropriate PDF headers.
    temp = BytesIO()
    p = canvas.Canvas(temp)
    # Create the PDF object, using the response object as its "file."
    p.drawString(100, 100, 'Book')
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.showPage()
    # Close the PDF object cleanly, and we're done.
    p.save()
    response.write(temp.getvalue())
    return response
