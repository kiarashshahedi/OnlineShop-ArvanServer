from django import template

register = template.Library()

@register.filter
def toman_format(value):
    value = int(value)  # Convert to integer to remove decimal places
    formatted_value = '{:,.0f}'.format(value)  # Format with thousand separators
    return formatted_value