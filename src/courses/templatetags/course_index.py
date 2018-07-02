from django import template
from ..models import Course

register = template.Library()


@register.simple_tag(takes_context=True)
def index(context, course):
    return Course.objects.all().filter(course_code=course)[0].pk
