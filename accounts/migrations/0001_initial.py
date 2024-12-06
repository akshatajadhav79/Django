# Generated by Django 4.2.4 on 2023-12-14 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingMaster',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.IntegerField()),
                ('address', models.TextField()),
                ('bookingDate', models.DateField(auto_now_add=True)),
                ('stayTo', models.DateField(auto_now=True)),
                ('stayFrom', models.DateField(auto_now=True)),
                ('peopel', models.CharField(choices=[('1 Person', '1 Person'), ('2 People', '2 People'), ('3 People', '3 People'), ('4 People', '4 People'), ('5 People', '5 People'), ('6 People', '6 People'), ('7 People', '7 People'), ('8 People', '8 People'), ('9 People', '9 People'), ('10 People', '10 People')], max_length=100)),
                ('message', models.TextField()),
                ('services', models.CharField(max_length=200)),
                ('advature', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='contactMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='admin', max_length=50, unique=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.IntegerField(blank=True, null=True, unique=True)),
                ('user_profile_image', models.ImageField(blank=True, upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceMaster',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('sevrice_name', models.CharField(max_length=200)),
                ('sevrice_details', models.TextField()),
                ('service_cost', models.PositiveIntegerField()),
                ('service_img', models.FileField(upload_to='servicesImg')),
                ('user', models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('email_token', models.CharField(blank=True, max_length=6, null=True)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.myuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdvatureMaster',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('adv_name', models.CharField(max_length=200)),
                ('adv_details', models.TextField()),
                ('adv_charges', models.PositiveIntegerField()),
                ('user', models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
