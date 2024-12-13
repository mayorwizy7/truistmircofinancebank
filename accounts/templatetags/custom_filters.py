from django import template

register = template.Library()

@register.filter
def hide_card_number(value):
    # Check if the value is a string and has at least 4 characters
    if isinstance(value, str) and len(value) >= 4:
        # Replace the middle characters with asterisks
        return value[:2] + '*' * (len(value) - 4) + value[-2:]
    else:
        return value
