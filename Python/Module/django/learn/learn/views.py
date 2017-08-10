from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import Template, Context
from django.template.loader import get_template
from datetime import datetime, timedelta
from django.template import RequestContext
from learn.forms import ContactForm


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


def display_meta(request, key):
    try:
        value = request.META[str(key)]
    except KeyError:
        values = list(request.META.items())
        values.sort()
        return render_to_response('display_meta.html', {'values': values})
    return render_to_response('display_meta.html', locals())


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['to@example.com'],
                fail_silently=True
            )
            # https://docs.djangoproject.com/en/1.11/topics/email/
            return HttpResponseRedirect('/')
    return render(request, 'contact.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'email': request.POST.get('email', ''),
        'message': request.POST.get('message', ''),
    })
    # csrf need use render


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactForm(
            initial={'subject': 'Untitled'}
        )
    return render(request, 'contact_form.html', {'form': form})
