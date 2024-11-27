# custom_filters.py
from django import template

register = template.Library()

@register.filter
def format_duration(duration):
    if duration:
        # คำนวณนาทีและวินาทีจาก TimeField
        minutes = duration.hour * 60 + duration.minute
        seconds = duration.second
        return f"{minutes:02}:{seconds:02}"
    return "00:00"
