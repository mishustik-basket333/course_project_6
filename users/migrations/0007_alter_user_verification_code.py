# Generated by Django 4.2.3 on 2023-07-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default='a3drs15Pows42', max_length=35, verbose_name='код верификации'),
        ),
    ]
