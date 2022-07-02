from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User, AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Register your models here.

class Profile(models.Model):
    TYPE_CHOICES = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )
    user_type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='PF',
    )
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_surname = models.CharField(max_length=256)
    # user_username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(gettext_lazy('email address'), unique=True)
    is_email_verified = models.BooleanField(default=False)
    phone_number = models.IntegerField()
    cpf = models.IntegerField(unique=True, blank=True)
    cnpj = models.IntegerField(unique=True, blank=True)
    fantasy_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=256)
    area = models.IntegerField(blank=True)

    def __str__(self):
        return self.cpf

# class Vehicle(models.Model):

#     TYPE_CATEGORY = (
#         ('Simples', 'Simples'),
#         ('Perecível', 'Perecível'),
#         ('Alto Valor', 'Alto Valor'),
#         ('Frágil', 'Frágil'),
#         ('Perigosa', 'Perigosa'),  # Add more shipping types later and review the current
#     )
#     TYPE_FUEL = (
#         ('Flex', 'Flex'),
#         ('Disel', 'Disel'),
#         ('Alcool', 'Alcool'),
#         ('Gasolina', 'Gasolina'),
#         ('Eletrico', 'Eletrico'),  # Add more shipping types later and review the current
#     )
#     vehicle_plate = models.CharField(max_length=20, unique=True)
#     vehicle_model = models.CharField(max_length=30)
#     vehicle_category = models.CharField(max_length=20, choices = TYPE_CATEGORY)
#     vehicle_document = models.CharField(max_length=20, unique=True)
#     vehicle_renavam = models.CharField(max_length=20, unique=True)
#     vehicle_chassi = models.CharField(max_length=20, unique=True)
#     vehicle_fuel = models.CharField(max_length=20, choices = TYPE_FUEL)
#     vehicle_license = models.CharField(max_length=20)
#     vehicle_color = models.CharField(max_length=20)
#     model_year = models.IntegerField()
#     manufacture_year = models.IntegerField()


#     user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.vehicle_model


# class Shipping(models.Model):

#     user_posted = models.ForeignKey(NewUser,on_delete=models.CASCADE, unique=True)
#     user_transporter = models.ForeignKey(NewUser,unique=True, blank=True)
#     # vehicle = models.ForeignKey(Vehicle,unique=True, blank=True) #Veículo que vai transportar a carga
#     # auction = models.ForeignKey(Auction, unique=True) # Leilão criado
#     title = models.CharField(max_length=100)
#
#     TYPE_SHIPPING = (
#         ('Simples', 'Simples'),
#         ('Perecível', 'Perecível'),
#         ('Alto Valor', 'Alto Valor'),
#         ('Frágil', 'Frágil'),
#         ('Perigosa', 'Perigosa'),  # Add more shipping types later and review the current
#     )
#     shipping_type = models.CharField(
#         max_length=15,
#         choices=TYPE_SHIPPING,
#         default='Simples',
#     )
#
#     deadline = models.DateTimeField()
#     delivery_location = models.CharField(max_length=100)
#     departure_location = models.CharField(max_length=100)
#     distance = models.IntegerField()  # In Km
#     post_date = models.DateTimeField(auto_now_add=True)
#     load_specifications = models.TextField()
#     cargo_weight = models.IntegerField(blank=True)  # In Kg
#     width = models.IntegerField(blank=True)  # In m
#     length = models.IntegerField(blank=True)  # In m
#     height = models.IntegerField(blank=True)  # In m
#     opening_bid = models.IntegerField(blank=True)
#
#     # load_value (...) Use Choice
#     at_auction = models.BooleanField()
#
#     def __str__(self):
#         return self.title


# def number_of_ratings(self):
#     ratings = Rating.objects.filter(user=self)
#     return len(ratings)
#
# def avg_rating(self):
#     sum = 0
#     ratings = Rating.objects.filter(user=self)
#     for rating in ratings:
#         sum += rating.stars
#     if len(ratings) > 0:
#         return sum / len(ratings)
#     else:
#         return 0
#


# class Rating(models.Model):
#     shipping_rated = models.ForeignKey(Shipping, on_delete=models.CASCADE)
#     user_transporter = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     user_posted = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     comment = models.TextField()

#     class Meta:
#         unique_together = (('shipping', 'user', 'user'),)
#         index_together = (('shipping', 'user', 'user'),)

# class Chat(models.Model):
#     user_client = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     user_transporter = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     conversation_log = models.TextField() # Pensar como armazenar o log e as mensagens da conversa em si
#     messages = models.TextField()


# class Documents(models.Model):
#     user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     document_image = models.ImageField(upload_to='')


# class Auction(models.Model):
#     user_who_offered = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     user_who_demanded = models.ForeignKey(NewUser, on_delete=models.CASCADE)
#     bid = models.IntegerField()
#     deadline = models.DateTimeField()

