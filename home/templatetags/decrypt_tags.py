from django import template
from home.encrypt_util import decrypt

register = template.Library()


@register.filter
def decrypt_template_tag(value):
    return decrypt(value)
