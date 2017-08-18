from django.conf.urls import url
from books.views import search, PublisherList, PublisherBookList


urlpatterns = [
    url(r'search/$', search),
    url(r'^publishers/$', PublisherList.as_view()),
    url(r'^publishers/([\w\s]+)/$', PublisherBookList.as_view()),
]
