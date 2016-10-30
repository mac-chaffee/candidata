from django import template
import locale

register = template.Library()

@register.simple_tag
def nice_format(number):
	return locale.currency(number, grouping=True)
 
