# Generated by Django 4.0.5 on 2022-07-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_shipping_cargo_weight_alter_shipping_distance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_type', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], default='PF', max_length=2)),
                ('user_name', models.CharField(max_length=100)),
                ('user_surname', models.CharField(max_length=256)),
                ('user_username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_email_verified', models.BooleanField(default=False)),
                ('phone_number', models.IntegerField(unique=True)),
                ('cpf', models.IntegerField(blank=True, unique=True)),
                ('cnpj', models.IntegerField(blank=True, unique=True)),
                ('fantasy_name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=256)),
                ('area', models.IntegerField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
    ]
