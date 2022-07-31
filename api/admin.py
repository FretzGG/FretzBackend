from django.contrib import admin
from .models import Chat, Rating, Profile, Vehicle, Shipping, Documents, Auction, Message
# Register your models here.


admin.site.register(Rating)
admin.site.register(Profile)
admin.site.register(Vehicle)
admin.site.register(Shipping)
admin.site.register(Documents)
admin.site.register(Auction)
admin.site.register(Chat)
admin.site.register(Message)
