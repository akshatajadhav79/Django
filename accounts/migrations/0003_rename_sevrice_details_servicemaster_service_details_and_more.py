# Generated by Django 4.2.4 on 2023-12-15 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_advaturemaster_user_alter_servicemaster_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicemaster',
            old_name='sevrice_details',
            new_name='service_details',
        ),
        migrations.RenameField(
            model_name='servicemaster',
            old_name='sevrice_name',
            new_name='service_name',
        ),
    ]
