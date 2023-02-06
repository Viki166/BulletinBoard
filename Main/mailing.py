from django.core.mail import send_mail
from BulletinBoard.settings import EMAIL_HOST_USER, ALLOWED_HOSTS
from News.models import News, Category
from Main.models import Contact


def newsletter_subscription(user_email):
    if user_email not in Contact.objects.all().values_list('email',flat=True):
        send_mail(
            "Вы подписались на рассылку",
            "Спасибо за подписку, каждую неделю вы будете получать письмо о свежих новостях!",
            EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
            )
    else:
        send_mail(
            "Вы уже подписаны на рассылку",
            "Каждую неделю вы получаете письмо о свежих новостях!",
            EMAIL_HOST_USER,
            [user_email],
            fail_silently=False,
            )



def newsletter():
    news = News.objects.all().order_by('-id')[0]
    link = ALLOWED_HOSTS[0]+ '/news/'+ news.pk
    contact_list = Contact.objects.all().values_list('email',flat=True).distinct()
    news_list = []
    for category in Category.objects.all():
        news_list.append(News.objects.all().order_by('-id').filter(category = category).values_list('header',flat=True)[0]) 
    send_mail(
    'Свежие новости',
    'f{news.header}. Пройдите по <a href={link}>ссылке</a>',
    EMAIL_HOST_USER,
    [contact_list],
    fail_silently=False
    )
g= Contact.objects.all().values_list('email',flat=True).distinct()
for i in Contact.objects.all().values_list('email',flat=True).distinct():
    pass
    #print(i)
# print(list(g))

# for cat in Category.objects.all():
#     print(News.objects.filter(category=cat.name))
m = News.objects.all().order_by('category')
# print(m)
# news_list = []
# for category in Category.objects.all():
#     news2 = News.objects.all().order_by('-id').filter(category = category).values_list('header',flat=True)[0]
#     # print(news2)
#     news_list.append(news2)

# print(news_list)

print(Contact.objects.all().values_list('email',flat=True))
if 'vika49661@mail.ru' in Contact.objects.all().values_list('email',flat=True):
    print('EST')
else:
    print('NET')