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
        fields = ('id', 'user_who_offered', 'user_who_demanded', 'bid', 'deadline')


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ('id', 'title', 'user_posted', 'user_transporter', 'vehicle', \
                  'at_auction', 'shipping_type', 'shipping_status', 'deadline', \
                  'delivery_location', 'departure_location')


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
        # token = Token.objects.create(user=user)
        return user


class RatingSerializer(serializers.ModelSerializer):

    profile_evaluator = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Profile.objects.all())
    profile_evaluated = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Profile.objects.all())

    class Meta:
        model = Rating
        fields = ('id', 'profile_evaluator', 'profile_evaluated', 'shipping', 'comment', 'stars', 'rating_date_time')


class ChatSerializer(serializers.ModelSerializer):
    # user_one = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Profile.objects.all())
    # user_two = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Profile.objects.all())

    class Meta:
        model = Chat
        fields = ['id', 'user_one', 'user_two', 'shipping']

class MessageSerializer(serializers.ModelSerializer):
    # sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    # receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp']
