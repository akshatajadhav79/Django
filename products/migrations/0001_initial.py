# Generated by Django 4.2.4 on 2023-11-29 17:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(unique=True)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField(default=0)),
                ('product_demo_price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMetaInformation',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('product_measuring', models.CharField(blank=True, choices=[('KG', 'KG'), ('ML', 'ML'), ('L', 'L'), (None, None)], max_length=100, null=True)),
                ('product_quality', models.CharField(blank=True, max_length=100, null=True)),
                ('is_restirct', models.BooleanField(blank=True, null=True)),
                ('restrict_quantity', models.IntegerField()),
                ('Product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta_info', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PoroductImages',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('product_images', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]