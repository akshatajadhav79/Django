# Generated by Django 3.1.12 on 2024-12-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_bookingmaster_phno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmaster',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
