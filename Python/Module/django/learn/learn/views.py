from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import get_template
from datetime import datetime, timedelta


def index(request):
    html = "<html><body>Hello,World!</body></html>"
    return HttpResponse(html)


def current_datetime(request):
    now = datetime.now()
    t = Template("<html><body>It is {{ current_date }} now.</body></html>")
    html = t.render(Context({'current_date': str(now)}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    # assert False  # debug break
    t = get_template('hours_ahead.html')
    html = t.render({'hour_offset': offset, 'next_time': str(dt)})
    return HttpResponse(html)


def hours_ahead2(request, hour_offset):
    try:
        hour_offset = int(hour_offset)
    except ValueError:
        raise Http404()
    next_time = datetime.now() + timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html', locals())  # locals() return all variable
    # No get_template, Template, HttpResponse, Context
