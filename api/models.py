from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    TYPE_CHOICES = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )
    user_type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='PF',
    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(gettext_lazy('email address'), unique=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    cpf = models.IntegerField(unique=True, blank=True, null=True)
    cnpj = models.IntegerField(unique=True, blank=True, null=True)
    fantasy_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=256, blank=True)
    area = models.IntegerField(unique=True, blank=True, null=True)

    # def number_of_ratings(self):
    #     ratings = Rating.objects.filter(Profile=self)
    #     return len(ratings)
    #
    # def avg_rating(self):
    #     sum = 0
    #     ratings = Rating.objects.filter(Profile=self)
    #     for rating in ratings:
    #         sum += rating.stars
    #     if len(ratings) > 0:
    #         return sum / len(ratings)
    #     else:
    #         return 0

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)


class Vehicle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TYPE_CATEGORY = (
        ('Simples', 'Simples'),
        ('Perecível', 'Perecível'),
        ('Alto Valor', 'Alto Valor'),
        ('Frágil', 'Frágil'),
        ('Perigosa', 'Perigosa'),  # Add more shipping types later and review the current
    )
    TYPE_FUEL = (
        ('Flex', 'Flex'),
        ('Disel', 'Disel'),
        ('Alcool', 'Alcool'),
        ('Gasolina', 'Gasolina'),
        ('Eletrico', 'Eletrico'),
    )
    vehicle_plate = models.CharField(max_length=20, blank=True, unique=True)
    vehicle_model = models.CharField(max_length=30, blank=True)
    vehicle_category = models.CharField(max_length=20, choices=TYPE_CATEGORY, default='Flex')
    vehicle_document = models.CharField(max_length=20, blank=True, unique=True)
    vehicle_renavam = models.CharField(max_length=20, blank=True, unique=True)
    vehicle_chassi = models.CharField(max_length=20, blank=True, unique=True)
    vehicle_fuel = models.CharField(max_length=20, choices=TYPE_FUEL, default='Simples')
    vehicle_license = models.CharField(max_length=30, blank=True)
    vehicle_color = models.CharField(max_length=30, blank=True)
    model_year = models.IntegerField(blank=True, null=True)
    manufacture_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.vehicle_plate


class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_DOCUMENT = (
        ('RG', 'RG'),
        ('CNH', 'CNH'),
    )
    document_type = models.CharField(max_length=20, choices=TYPE_DOCUMENT, default='')
    # document_image = models.ImageField(upload_to='')


class Auction(models.Model):
    user_who_offered = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_who_offered', default='')
    user_who_demanded = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_who_demanded', default='')
    bid = models.IntegerField(blank=True, null=True)
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return 'Leilão ' + str(self.id)


class Shipping(models.Model):
    title = models.CharField(max_length=100)

    user_posted = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posted', default='')
    user_transporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transporter', default='')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Veículo que vai transportar a carga
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)  # Leilão criado

    TYPE_SHIPPING = (
        ('Simples', 'Simples'),
        ('Perecível', 'Perecível'),
        ('Alto Valor', 'Alto Valor'),
        ('Frágil', 'Frágil'),
        ('Perigosa', 'Perigosa'),  # Add more shipping types later and review the current
    )
    shipping_type = models.CharField(
        max_length=15,
        choices=TYPE_SHIPPING,
        default='Simples',
    )

    deadline = models.DateTimeField(null=True)
    delivery_location = models.CharField(max_length=100, blank=True)
    departure_location = models.CharField(max_length=100, blank=True)
    distance = models.IntegerField(blank=True, null=True)  # In Km
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    load_specifications = models.TextField(blank=True)
    cargo_weight = models.IntegerField(blank=True, null=True)  # In Kg
    width = models.IntegerField(blank=True, null=True)  # In m
    length = models.IntegerField(blank=True, null=True)  # In m
    height = models.IntegerField(blank=True, null=True)  # In m
    opening_bid = models.IntegerField(blank=True, null=True)

    # load_value (...) Use Choice
    at_auction = models.BooleanField()

    # def posted_by(self):
    #     user_posted = User.objects.filter(user=self)
    #     return user_posted

    class Meta:
        unique_together = (('user_posted', 'user_transporter'),)
        index_together = (('user_posted', 'user_transporter'),)

    def __str__(self):
        return self.title


# class Movie(models.Model):
#     title = models.CharField(max_length=32)
#     description = models.TextField(max_length=360)
#
#     def number_of_ratings(self):
#         ratings = Rating.objects.filter(movie=self)
#         return len(ratings)
#
#     def avg_rating(self):
#         sum = 0
#         ratings = Rating.objects.filter(movie=self)
#         for rating in ratings:
#             sum += rating.stars
#         if len(ratings) > 0:
#             return sum / len(ratings)
#         else:
#             return 0

class Rating(models.Model):
    # Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # class Meta:
    #     unique_together = (('user'),)
    #     index_together = (('user'),)
