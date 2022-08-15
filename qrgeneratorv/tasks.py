
from celery import shared_task
from django.core.mail import send_mail
from .models import QrCode, Tariff, Template, User
users = User.objects.all()
from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum
from qrcored import settings

@shared_task(bind=True)
def send_beat_email(*args, **kwargs):
    for user in users:
        date_time_limit = user.tariff.sms_service
        limit_time = user.created_date + timedelta(days=date_time_limit)
            # date_find += timedelta(days=sms_data.days)
        if timezone.now() > limit_time:
            limit_time += timedelta(days=date_time_limit)
            templates_of_user = Template.objects.filter(user=user)

            message_text = f"\
            Qrcodes count of this user: {user.qrcodes.count()}\n\
            This is scaners count: {QrCode.objects.filter(user=user).aggregate(Sum('url_counter'))['url_counter__sum']}\n\
            Count of enter to 1 - social network: {templates_of_user.aggregate(Sum('social_media_type1_url_counter'))['social_media_type1_url_counter__sum']}\n\
            Count of enter to 2 - social network: {templates_of_user.aggregate(Sum('social_media_type2_url_counter'))['social_media_type2_url_counter__sum']}\n\
            Count of enter to 3 - social network: {templates_of_user.aggregate(Sum('social_media_type3_url_counter'))['social_media_type3_url_counter__sum']}"
            send_mail(
                'This is beat task',
                message_text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
                )
        else:
            continue
    return "Email sent"
        # else:
        #     continue