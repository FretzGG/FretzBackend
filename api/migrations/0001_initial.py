# Generated by Django 4.0.5 on 2022-06-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('shipping_type', models.CharField(choices=[('Simples', 'Simples'), ('Perecível', 'Perecível'), ('Alto Valor', 'Alto Valor'), ('Frágil', 'Frágil'), ('Perigosa', 'Perigosa')], default='Simples', max_length=15)),
                ('deadline', models.DateTimeField()),
                ('delivery_location', models.CharField(max_length=100)),
                ('departure_location', models.CharField(max_length=100)),
                ('distance', models.IntegerField(max_length=10)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('load_specifications', models.TextField()),
                ('cargo_weight', models.IntegerField(blank=True, max_length=10)),
                ('width', models.IntegerField(blank=True, max_length=10)),
                ('length', models.IntegerField(blank=True, max_length=10)),
                ('height', models.IntegerField(blank=True, max_length=10)),
                ('opening_bid', models.IntegerField(blank=True, max_length=10)),
                ('at_auction', models.BooleanField()),
            ],
        ),
    ]