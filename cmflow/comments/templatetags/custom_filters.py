import html

from django import template

from ..models import Like

register = template.Library()


@register.filter(name="startswith")
def startswith(text, starts):
    if isinstance(text, str):
        return text.startswith(starts)
    return False


@register.filter(name="user_has_liked")
def user_has_liked_comment(comment, user):
    return Like.objects.filter(comment=comment, user=user).exists()


@register.filter(name="escape_html")
def escape_html(value):
    return html.unescape(value)
