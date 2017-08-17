from django.conf.urls import url
from books.views import search, PublisherList


urlpatterns = [
    url(r'search/$', search),
    url(r'^publishers/$', PublisherList.as_view()),
]
