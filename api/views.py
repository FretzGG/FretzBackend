from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Rating, Profile, Vehicle, Shipping, Documents, Message
from .serializers import RatingSerializer, UserSerializer, ProfileSerializer, VehicleSerializer, \
    ShippingSerializer, DocumentsSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.db.models import Q

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Token 714903b38a102a0b5448d655e3cec9daf611b4dd

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.name = 'Joao'
        user.save()


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False)
    def get_user_ratings(self, request):
        if 'profile_evaluated' in request.data:
            ratings = Rating.objects.filter(profile_evaluated=request.data['profile_evaluated'])
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'profile_evaluated': 'Este campo é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, *args, **kwargs):
    #     response = {'message': 'not able to update through this method'}
    #     return Response(response, status=status.HTTP_400_BAD_REQUEST)
    #
    # def create(self, request, *args, **kwargs):
    #     response = {'message': 'not able to create through this method'}
    #     return Response(response, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False)
    def get_chat(self, request):
        if ('sender' in request.data) and ('receiver' in request.data):

            # messages = Message.objects.filter(sender=request.data['sender'], receiver=request.data['receiver'])
            criterion1 = Q(sender=request.data['sender'], receiver=request.data['receiver'])
            criterion2 = Q(sender=request.data['receiver'], receiver=request.data['sender'])
            messages = Message.objects.filter(criterion1 | criterion2)
            serializer = MessageSerializer(messages, many=True)

            for message in messages:
                message.is_read = True
                message.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'sender': 'Este campo é obrigatório', 'receiver': 'Este campo é obrigatório'},
                            status=status.HTTP_400_BAD_REQUEST)

        # if request.method == 'GET':
        #     messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        #     serializer = MessageSerializer(messages, many=True, context={'request': request})
        #     for message in messages:
        #         message.is_read = True
        #         message.save()
        #     return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def message_list(request, sender=None, receiver=None):
#     """
#     List all required messages, or create a new message.
#     """
#     if request.method == 'GET':
#         messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
#         serializer = MessageSerializer(messages, many=True, context={'request': request})

#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MessageSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (AllowAny,)
#
#     @action(detail=True, methods=['POST'])
#     def rate_movie(self, request, pk=None):
#         if 'stars' in request.data:  # validate request data
#
#             movie = Movie.objects.get(id=pk)  # select obj from db
#             stars = request.data['stars']
#             user = request.user
#
#             try:
#                 rating = Rating.objects.get(user=user.id, movie=movie.id)
#                 rating.stars = stars
#                 rating.save()
#                 serializer = RatingSerializer(rating, many=False)
#                 response = {'message': 'Rating updated', 'result': serializer.data}
#                 return Response(response, status=status.HTTP_200_OK)
#             except:
#                 Rating.objects.create(user=user, movie=movie, stars=stars)
#                 serializer = RatingSerializer(rating, many=False)
#                 response = {'message': 'Rating crated', 'result': serializer.data}
#                 return Response(response, status=status.HTTP_200_OK)
#
#         else:
#             response = {'message': 'missing stars'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
#
