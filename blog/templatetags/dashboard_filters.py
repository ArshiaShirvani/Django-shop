from django import template
from khayyam import JalaliDatetime


register = template.Library()

@register.filter
def to_jalali(value):
    if value:
        return JalaliDatetime(value).strftime('%Y/%m/%d - %H:%M')
    return ""