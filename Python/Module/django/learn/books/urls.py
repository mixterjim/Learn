from django.conf.urls import url
from books.views import *

urlpatterns = [
    url(r'^$', PublisherList.as_view()),
    url(r'^search/$', search),
    url(r'^([\w\s]+)/$', PublisherBookList.as_view()),
    url(r'^down/csv/$', books_csv),
    url(r'^down/pdf/$', books_pdf),
]
