# Generated by Django 4.2.3 on 2023-07-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default='s1Po34s2rw5da', max_length=35, verbose_name='код верификации'),
        ),
    ]
