# Generated by Django 4.2.5 on 2023-10-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApplication', '0006_alter_news_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Изменено'),
        ),
    ]
