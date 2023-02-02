from django.core.mail import send_mail
from Main.mailing import newsletter_subscription
from BulletinBoard.celery import app
from Main.models import Contact
from BulletinBoard.settings import EMAIL_HOST_USER, ALLOWED_HOSTS
from News.models import News, Category



@app.task
def send_email(user_email):
    newsletter_subscription(user_email)


# @app.task
# def task_newsletter():
#     list_contacts = []
#     news = News.objects.all().order_by('-id')[0]
#     link = ALLOWED_HOSTS[0]+ '/news/'+ f'{news.pk}'
#     # print('contacts: ',list_contacts)
#     for contact in Contact.objects.all():
#         list_contacts.append(contact)
#     # print("LIST ",set(list_contacts))
#     send_mail(
#         'Свежие новости',
#         "Новые новости на сайте",
#         EMAIL_HOST_USER,
#         list(set(list_contacts)),
#         fail_silently=False
#         )