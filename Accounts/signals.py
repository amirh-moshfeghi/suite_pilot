import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

log = logging.getLogger(__name__)

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):

    ip = request.META.get('REMOTE_ADDR')

    log.debug('login user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')

    log.debug('logout user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    log.warning('login failed for: {credentials}'.format(
        credentials=credentials,
    ))