"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from learn.views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),  # hours_ahead2
    url(r'^meta/cookie$', display_meta, {'key': 'HTTP_COOKIE'}),
    url(r'^meta/(?P<key>[\w.]*)$', display_meta,),  # return argument in (?P<name>pattern)
    url(r'^books/', include('books.urls')),
    url(r'^contact/$', contact),
    url(r'^contact_form/$', contact_form),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^about/(\w+)/$', about_pages),
]
if settings.DEBUG:
    urlpatterns += (
        # (r'^debuginfo/$', debug),
    )
