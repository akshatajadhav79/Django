# Generated by Django 4.2.4 on 2023-12-13 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_poroductimages_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmetainformation',
            name='Product',
        ),
        migrations.DeleteModel(
            name='PoroductImages',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductMetaInformation',
        ),
    ]
