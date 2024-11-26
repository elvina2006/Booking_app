from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'hotels', HotelListViewSet, basename='Hotel-list')
router.register(r'user', UserProfileViewSet, basename='user-list')
router.register(r'room', RoomListViewSet, basename='room-list')
router.register(r'room_detail', RoomDetailViewSet, basename='room-detail')
router.register(r'booking', BookingViewSet, basename='booking-list')
router.register(r'review', ReviewViewSet, basename='review-list')
router.register(r'room_image', RoomImageViewSet, basename='room-image')

urlpatterns = [
    path('', include(router.urls))
]
