from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.template import Template, TemplateDoesNotExist, Context, RequestContext
from django.template.loader import get_template
from datetime import datetime, timedelta
from learn.forms import ContactForm


def custom_proc(request):
    "A context processor that provides 'user' and 'ip_address'."
    return {
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
    }


def index(request):
    t = get_template('index.html')
    html = t.render(custom_proc(request))
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
                fail_silently=True
            )
            return HttpResponseRedirect('/')
    else:
        form = ContactForm(
            initial={'subject': 'Untitled'}
        )
    return render(request, 'contact_form.html', {'form': form})


def about_pages(request, page):
    try:
        return render(request, "about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()


def cookie(request):
    s = {}
    if "favorite_color" in request.GET or "favorite_color" in request.COOKIES:
        if "favorite_color" in request.GET:
            request.COOKIES["favorite_color"] = request.GET["favorite_color"]
            # color = request.GET["favorite_color"]
            # response = HttpResponse("Your favorite color is now %s" % color)
            # response.set_cookie("favorite_color", request.GET["favorite_color"])
            # return response
        color = request.COOKIES["favorite_color"]
        s = {'message': "Your favorite color is " + color + '.'}
    return render_to_response('favorite_color.html', s)


def session(request):
    s = {}
    if "favorite_color" in request.GET or "favorite_color" in request.session:
        if "favorite_color" in request.GET:
            request.session["favorite_color"] = request.GET["favorite_color"]
        color = request.session["favorite_color"]
        s = {'message': "Your favorite color is " + color + '.'}
    return render_to_response('favorite_color.html', s)


def user_logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("account loggedout")


def login_result(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponse("account loggedin")
    else:
        # Show an error page
        return HttpResponse("account invalid")


# @login_required
def accounts(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
        # or use @login_required
    else:
        return HttpResponse("Hello " + request.user.username)


def vote(request):
    if request.user.is_authenticated() and request.user.has_perm('polls.can_vote')):
        # vote here
    else:
        return HttpResponse("You can't vote in this poll.")
def user_can_vote(user):
    return user.is_authenticated() and user.has_perm("polls.can_vote")

@user_passes_test(user_can_vote, login_url = "/login/")
def vote(request):
    # Code here can assume a logged-in user with the correct permission.
