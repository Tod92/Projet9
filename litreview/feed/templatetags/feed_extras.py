from django import template


"""
permet d'utiliser un filtre personnalisé, ici :
{{ instance|model_type }}
nous retournera le nom de la classe en str
"""

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__
