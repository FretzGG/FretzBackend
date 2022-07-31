# Generated by Django 4.0.5 on 2022-07-31 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_alter_shipping_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='user_transporter',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_transporter', to=settings.AUTH_USER_MODEL),
        ),
    ]
