# Generated by Django 4.2.1 on 2023-05-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_useraccountmodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccountmodel',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/ava3.webp', null=True, upload_to='avatars/'),
        ),
    ]