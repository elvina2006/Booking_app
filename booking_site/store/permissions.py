from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckCRUD(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'


class CheckHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckRoom(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.room_status == 'свободен':
            return True
        return False


class CheckBooking(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'simpleUser':
            return True
        return False


class CheckReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user_name


class CheckRoomOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.hotel_room.owner


class CheckBookUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user_book:
            return True
        return False


class CheckImages(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
