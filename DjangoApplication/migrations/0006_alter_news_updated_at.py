# Generated by Django 4.2.5 on 2023-10-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApplication', '0005_news_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Изменено'),
        ),
    ]