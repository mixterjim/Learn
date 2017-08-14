from django import template
import datetime

register = template.Library()


class CurrentTimeNode(template.Node):

    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)


def cut(value, arg):
    "Removes all values of arg from the given string"
    return value.replace(arg, '')
register.filter('cut', cut)


@register.filter
def lower(value):  # Only one argument.
    return value.lower()


@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])
