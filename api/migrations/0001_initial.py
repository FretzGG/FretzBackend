# Generated by Django 4.0.5 on 2022-07-31 20:17

import api.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('PF', 'Pessoa Física'), ('PT', 'Pessoa Transportadora'), ('PJ', 'Pessoa Jurídica')], default='PF', max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='email address')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('phone_number', models.IntegerField(blank=True, null=True, unique=True)),
                ('cpf', models.IntegerField(blank=True, null=True, unique=True)),
                ('cnpj', models.IntegerField(blank=True, null=True, unique=True)),
                ('fantasy_name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('area', models.IntegerField(blank=True, null=True, unique=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=api.models.update_profile_pic)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_license_plate', models.CharField(blank=True, max_length=20, unique=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=30)),
                ('vehicle_category', models.CharField(choices=[('Simples', 'Simples'), ('Pesado', 'Pesado'), ('Perecível', 'Perecível'), ('Alto Valor', 'Alto Valor'), ('Frágil', 'Frágil'), ('Perigosa', 'Perigosa')], default='Simples', max_length=20)),
                ('vehicle_color', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('at_auction', models.BooleanField(default=True)),
                ('teste', models.BooleanField(default=True)),
                ('shipping_type', models.CharField(choices=[('Simples', 'Simples'), ('Perecível', 'Perecível'), ('Alto Valor', 'Alto Valor'), ('Frágil', 'Frágil'), ('Perigosa', 'Perigosa')], default='Simples', max_length=15)),
                ('shipping_status', models.CharField(choices=[('Ativo', 'Ativo'), ('Em Progresso', 'Em Progresso'), ('Finalizado', 'Finalizado')], default='Ativo', max_length=15)),
                ('deadline', models.DateField()),
                ('delivery_location', models.CharField(max_length=100)),
                ('departure_location', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('load_specifications', models.TextField(blank=True)),
                ('cargo_weight', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('opening_bid', models.IntegerField(blank=True, null=True)),
                ('user_posted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posted', to=settings.AUTH_USER_MODEL)),
                ('user_transporter', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_transporter', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.vehicle')),
            ],
            options={
                'unique_together': {('user_posted', 'user_transporter')},
                'index_together': {('user_posted', 'user_transporter')},
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('profile_evaluated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_evaluated', to='api.profile')),
                ('profile_evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_evaluator', to='api.profile')),
                ('shipping', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.shipping')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.chat')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('RG', 'RG'), ('CNH', 'CNH'), ('CRV', 'CRV'), ('CRLV', 'CRLV')], default='', max_length=20)),
                ('document_image', models.ImageField(blank=True, null=True, upload_to=api.models.update_document_pic)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='shipping',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.shipping'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_one', to='api.profile'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_two', to='api.profile'),
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('shipping', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.shipping')),
                ('user_who_demanded', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_who_demanded', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
