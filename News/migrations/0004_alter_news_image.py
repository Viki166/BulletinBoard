# Generated by Django 4.1.5 on 2023-02-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]