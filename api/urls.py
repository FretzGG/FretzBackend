from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import RatingViewSet, ProfileViewSet, UserViewSet,VehicleViewSet, ShippingViewSet, DocumentsViewSet

router = routers.DefaultRouter()


router.register('users', UserViewSet)
router.register('ratings', RatingViewSet)
router.register('profile', ProfileViewSet)
router.register('vehicle', VehicleViewSet)
router.register('shipping', ShippingViewSet)
router.register('documents', DocumentsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
