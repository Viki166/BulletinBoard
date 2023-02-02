from django.core.mail import send_mail
from BulletinBoard.settings import EMAIL_HOST_USER
from News.models import News
from Main.models import Contact


def newsletter_subscription(user_email):
    send_mail(
        "Вы подписались на рассылку",
        "Спасибо за подписку, каждую неделю вы будете получать письмо о свежих новостях!",
        EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
        )


# def newsletter():
#     news = News.objects.all().order_by('-id')[0]
#     link = ALLOWED_HOSTS[0]+ '/news/'+ news.pk
#     for contact in Contact.objects.all():
#         send_mail(
#             'Свежие новости',
#             'f{news.header}. Пройдите по <a href={link}>ссылке</a>',
#             EMAIL_HOST_USER,
#             [contact.email],
#             fail_silently=False
#             )