# Generated by Django 3.0 on 2022-05-26 05:32

import app_layer.behavioural.validators
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empID', models.AutoField(primary_key=True, serialize=False)),
                ('empName', models.CharField(max_length=100, validators=[app_layer.behavioural.validators.validate_name])),
                ('empDOJ', models.DateField(auto_now_add=True, validators=[app_layer.behavioural.validators.validate_date])),
                ('empDescription', models.CharField(blank=True, max_length=250, validators=[app_layer.behavioural.validators.validate_empDescription])),
                ('empCategory', models.CharField(blank=True, max_length=100)),
                ('empCity', models.CharField(max_length=50)),
                ('empOfficeVenue', models.CharField(max_length=500)),
                ('empOrg', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_modified_date', models.DateTimeField(auto_now_add=True, verbose_name='last modified date')),
                ('display_name', models.CharField(blank=True, max_length=150, validators=[app_layer.behavioural.validators.validate_name], verbose_name='display name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'ordering': ('-date_joined',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['display_name'], name='app_layer_c_display_3fab39_idx'),
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['username'], name='app_layer_c_usernam_384330_idx'),
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['email'], name='app_layer_c_email_3907c7_idx'),
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['date_joined'], name='app_layer_c_date_jo_d59aa5_idx'),
        ),
    ]