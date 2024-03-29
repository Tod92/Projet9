from django import template
from django.utils import timezone

register = template.Library()

MINUTE_DELTA = timezone.timedelta(minutes=1)
HOUR_DELTA = timezone.timedelta(hours=1)
DAY_DELTA = timezone.timedelta(days=1)

STAR_EMPTY = "☆"
STAR_FULL = "★"


@register.filter
def model_type(value):
    """
    permet d'utiliser un filtre personnalisé, ici :
    {{ instance|model_type }}
    nous retournera le nom de la classe en str
    """
    return type(value).__name__

@register.filter
def star_rating_display(value):

    result = ""
    for s in range(value):
        result += STAR_FULL
    result += (5 - value) * STAR_EMPTY
    return result


@register.simple_tag(takes_context=True)
def get_posted_at_display(context, time):

    result = 'Posté '
    now = timezone.now()
    delta = now - time

    if delta > DAY_DELTA:
        result += 'le ' + time.strftime("%d/%m") + ' à ' + time.strftime("%H:%M")
    elif delta > HOUR_DELTA:
        result += 'il y a ' + str(int(delta.total_seconds() // 3600)) + ' heure(s)'
    elif delta > MINUTE_DELTA:
        result += 'il y a ' + str(int(delta.total_seconds() // 60 )) + ' minute(s)'
    else:
        result += 'il y a ' + str(int(delta.total_seconds())) + ' secondes(s)'

    return result
