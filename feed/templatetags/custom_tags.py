from atexit import register
from django import template
from feed.models import Notification
from profiles.models import Profile

register = template.Library()

@register.inclusion_tag('feed/show_notification.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    print("request_user:",request_user)
    # notifications = Notification.objects.filter(to_user = request_user).exclude(user_has_seen=True).order_by('-date')
    notifications = Notification.objects.filter(to_user = request_user, user_has_seen=False).order_by('-date')

    return {"notifications":notifications}
