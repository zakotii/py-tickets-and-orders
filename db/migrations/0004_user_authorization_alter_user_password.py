# Generated by Django 4.0.2 on 2024-05-11 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_user_order_alter_movie_title_ticket_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='authorization',
            field=models.CharField(default='admin.user', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='1qazcde3', max_length=50),
        ),
    ]