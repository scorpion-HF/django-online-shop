# Generated by Django 3.0.5 on 2020-04-26 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200426_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.baseuser',),
            managers=[
                ('object', users.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=13)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.baseuser',),
            managers=[
                ('object', users.managers.UserManager()),
            ],
        ),
    ]
