# Generated by Django 4.2.4 on 2024-01-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_myuser_alter_advaturemaster_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmaster',
            name='phno',
            field=models.BigIntegerField(),
        ),
    ]
