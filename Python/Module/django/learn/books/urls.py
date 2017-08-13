from django.conf.urls import url
from books.views import search

urlpatterns = [
    url(r'search/$', search),
]
