from django import template
import locale


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


register = template.Library()


@register.filter
def nice_format(number):
    return locale.currency(number, grouping=True)

