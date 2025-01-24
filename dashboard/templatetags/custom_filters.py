from django import template
from khayyam import JalaliDate

register = template.Library()

@register.filter
def to_jalali(value):
    if value:
        return JalaliDate(value).strftime('%Y/%m/%d - %H:%m')
    return ""