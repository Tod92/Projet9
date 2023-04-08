from django import template
from django.utils import timezone

register = template.Library()

MINUTE_DELTA = timezone.timedelta(minutes=1)
HOUR_DELTA = timezone.timedelta(hours=1)
DAY_DELTA = timezone.timedelta(days=1)


@register.filter
def model_type(value):
    """
    permet d'utiliser un filtre personnalisé, ici :
    {{ instance|model_type }}
    nous retournera le nom de la classe en str
    """
    return type(value).__name__

@register.simple_tag(takes_context=True)
def get_posted_at_display(context, time):

    result = 'Posté '
    now = timezone.now()
    delta = now - time

    if delta > DAY_DELTA:
        result += 'à ' + time.strftime("%H:%M:%S")
    elif delta > HOUR_DELTA:
        result += 'il y a ' + str(int(delta.total_seconds() // 3600)) + ' heure(s)'
    elif delta > MINUTE_DELTA:
        result += 'il y a ' + str(delta.minutes) + ' minute(s)'
    else:
        result += 'il y a ' + delta.strftime("%S") + ' seconde(s)'

    return result
