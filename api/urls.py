from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import AuctionViewSet, ChatViewSet, RatingViewSet, ProfileViewSet, UserViewSet, VehicleViewSet, ShippingViewSet, DocumentsViewSet, \
    MessageViewSet
from . import views

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('profile', ProfileViewSet)
router.register('vehicle', VehicleViewSet)
router.register('shipping', ShippingViewSet)
router.register('auction', AuctionViewSet)
router.register('documents', DocumentsViewSet)
router.register('ratings', RatingViewSet)
router.register('chat', ChatViewSet)
router.register('message', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),  # For GET request.
    # path('messages/', views.message_list, name='message-list'),   # For POST

]
