from rest_framework import serializers
from .models import Rating, Profile, Vehicle, Shipping, Documents, Auction
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'user', 'email', 'user_type', 'name', 'phone_number', 'cpf', 'cnpj', 'fantasy_name', 'address',
            'area')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'user', 'vehicle_plate', 'vehicle_model', 'vehicle_category', 'vehicle_fuel')


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('id', 'user', 'document_type')


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('id', 'user_who_offered', 'user_who_demanded', 'bid', 'deadline')


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ('id', 'title', 'user_posted', 'user_transporter', 'shipping_type')


# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('id', 'title', 'description', 'number_of_ratings', 'avg_rating')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'stars')
