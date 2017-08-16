from django import template
import datetime
import re
register = template.Library()


class CurrentTimeNode(template.Node):

    def __init__(self, format_string, var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''


@register.tag(name="current_time")
def do_current_time(parser, token):
    # This version uses a regular expression to parse tag contents.
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents[0]
        raise template.TemplateSyntaxError(msg)

    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        fmt, var_name = m.groups()
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)

    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode(fmt[1:-1], var_name)


# @register.simple_tag
# def current_time(format_string):
#     try:
#         return datetime.datetime.now().strftime(str(format_string))
#     except UnicodeEncodeError:
#         return ''


class UpperNode(template.Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()


@register.tag(name="upper")
def do_upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)


def cut(value, arg):
    "Removes all values of arg from the given string"
    return value.replace(arg, '')
register.filter('cut', cut)


@register.filter
def lower(value):  # Only one argument.
    return value.lower()
