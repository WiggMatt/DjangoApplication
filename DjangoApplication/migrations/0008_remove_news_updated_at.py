# Generated by Django 4.2.5 on 2023-10-20 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApplication', '0007_alter_news_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='updated_at',
        ),
    ]
