from django import template

register = template.Library()


@register.simple_tag()
def add_like_class(user, likes):
    for like_obj in likes:
        if like_obj.user == user:
            return ' text-danger'
    return ''
