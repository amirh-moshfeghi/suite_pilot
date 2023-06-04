from Accounts.models import User
from Notifications.models import Notification


def notifs_context_processor(request):
    notifs_count = Notification.objects.count()
    notifs = Notification.objects.all()[:3]
    return {
        'count_notifs_header': notifs_count,
        'notifs_header': notifs,
    }


def user_context_processor(request):
    users = User.objects.filter(is_active=True)

    return {
        'users': users,
    }