from rest_framework import serializers
from .models import Chat, Rating, Profile, Vehicle, Shipping, Documents, Auction, Message
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'name', 'user', 'email', 'user_type', 'name', 'phone_number', 'cpf', 'cnpj', 'fantasy_name',
            'address', 'area', 'profile_pic', 'number_of_ratings', 'avg_rating')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'user', 'vehicle_license_plate', 'vehicle_model', 'vehicle_category', 'vehicle_color')


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('id', 'user', 'document_type', 'document_image')


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('id', 'shipping', 'user_who_offered', 'bid', 'deadline')


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ('id', 'title', 'load_specifications', 'user_posted', 'user_transporter', \
                    'vehicle', 'at_auction', 'shipping_type', 'shipping_status', 'deadline', \
                    'delivery_location', 'departure_location', 'cargo_weight', 'width', 'length', \
                    'height', 'opening_bid')


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
        fields = ('id', 'profile_evaluator', 'profile_evaluated', 'shipping', 'comment', 'stars', 'date')


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'user_one', 'user_two', 'shipping']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'receiver', 'message', 'timestamp']
