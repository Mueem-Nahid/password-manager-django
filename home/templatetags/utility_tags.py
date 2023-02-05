from django import template

from home.utils import generate_random_password

register = template.Library()


@register.filter
def generate_random_password_tag():
    return generate_random_password()
