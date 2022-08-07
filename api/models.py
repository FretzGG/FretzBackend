from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets, status


def update_profile_pic(instance, filename):
    return f"profile_pic/{instance.id}-{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    TYPE_CHOICES = (
        ('PF', 'Pessoa Física'),
        ('PT', 'Pessoa Transportadora'),
        ('PJ', 'Pessoa Jurídica'),
    )

    user_type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='PF',
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(gettext_lazy('email address'), unique=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    cpf = models.IntegerField(unique=True, blank=True, null=True)
    cnpj = models.IntegerField(unique=True, blank=True, null=True)
    fantasy_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=256, blank=True)
    area = models.IntegerField(unique=True, blank=True, null=True)

    profile_pic = models.ImageField(upload_to=update_profile_pic, blank=True, null=True)

    def number_of_ratings(self):
        ratings = Rating.objects.filter(profile_evaluated=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(profile_evaluated=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return -1  # -1 indica que o usuário não possui avaliações

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        print("Teste")
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
        ('Perigosa', 'Perigosa'),
        ('Pesado', 'Pesado'),
        ('Refrigerada', 'Refrigerada')  # Add more shipping types later and review the current
    )
    vehicle_license_plate = models.CharField(max_length=20, blank=True, unique=True)
    vehicle_model = models.CharField(max_length=30, blank=True)
    vehicle_category = models.CharField(max_length=20, choices=TYPE_CATEGORY, default='Simples')
    vehicle_color = models.CharField(max_length=30, blank=True)

    # vehicle_document_number = models.CharField(max_length=20, blank=True, unique=True)

    def __str__(self):
        return f"{self.vehicle_license_plate} by {self.user}"


def update_document_pic(self, filename):
    return f"documents/{self.id}-{filename}"


class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_DOCUMENT = (
        ('RG', 'RG'),
        ('CNH', 'CNH'),
        ('CRV', 'CRV'),
        ('CRLV', 'CRLV'),  # (Insert Other Types)
    )
    document_type = models.CharField(max_length=20, choices=TYPE_DOCUMENT, default='')
    document_image = models.ImageField(upload_to=update_document_pic, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Shipping(models.Model):
    title = models.CharField(max_length=100)

    user_posted = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posted')
    user_transporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transporter', blank=True,
                                         null=True, default=None)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, blank=True,
                                null=True)  # Veículo que vai transportar a carga
    # auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True)  # Leilão criado
    at_auction = models.BooleanField(default=True)

    TYPE_SHIPPING = (
        ('Simples', 'Simples'),
        ('Perecível', 'Perecível'),
        ('Alto Valor', 'Alto Valor'),
        ('Frágil', 'Frágil'),
        ('Perigosa', 'Perigosa'),
        ('Pesado', 'Pesado'),
        ('Refrigerada', 'Refrigerada')  # Add more shipping types later and review the current

    )
    shipping_type = models.CharField(
        max_length=15,
        choices=TYPE_SHIPPING,
        default='Simples',
    )

    STATUS = (
        ('Ativo', 'Ativo'),
        ('Em Progresso', 'Em Progresso'),
        ('Finalizado', 'Finalizado'),
    )

    shipping_status = models.CharField(
        max_length=15,
        choices=STATUS,
        default='Ativo',
    )

    deadline = models.DateField()
    delivery_location = models.CharField(max_length=100)
    departure_location = models.CharField(max_length=100)
    # distance = models.IntegerField(blank=True, null=True)  # In Km
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    load_specifications = models.TextField(blank=True)
    cargo_weight = models.FloatField(blank=True, null=True)  # In Kg
    width = models.FloatField(blank=True, null=True)  # In m
    length = models.FloatField(blank=True, null=True)  # In m
    height = models.FloatField(blank=True, null=True)  # In m
    opening_bid = models.FloatField(blank=True, null=True)

    # load_value (...) Use Choice

    class Meta:
        unique_together = (('user_posted', 'user_transporter'),)
        index_together = (('user_posted', 'user_transporter'),)

    def __str__(self):
        return f"{self.title} posted by {self.user_posted}"


class Auction(models.Model):
    # user_who_offered = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_who_offered', default='')
    user_who_demanded = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_who_demanded', default='')
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, default='')
    bid = models.IntegerField()
    deadline = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Lance {self.id} referente ao frete {self.shipping.title}"


class Rating(models.Model):
    profile_evaluator = models.ForeignKey(Profile, related_name='profile_evaluator', on_delete=models.CASCADE)
    profile_evaluated = models.ForeignKey(Profile, related_name='profile_evaluated', on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, default='')

    rating_date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Rating {self.id} from {self.profile_evaluator} to {self.profile_evaluated} "

    # class Meta:
    #     unique_together = (('user'),)
    #     index_together = (('user'),)


class Chat(models.Model):
    user_one = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_one')
    user_two = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_two')
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"Chat {self.id} between {self.user_one} and {self.user_two}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default='')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)
