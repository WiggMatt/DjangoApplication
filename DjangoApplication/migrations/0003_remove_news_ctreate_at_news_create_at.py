# Generated by Django 4.2.5 on 2023-10-19 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApplication', '0002_alter_category_options_remove_news_is_published_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='ctreate_at',
        ),
        migrations.AddField(
            model_name='news',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время публикации'),
            preserve_default=False,
        ),
    ]