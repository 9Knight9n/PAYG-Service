from django.urls import path


urlpatterns = [
    path('api1/', api1.as_view(), name="admin's user management APIs"),

    path('api2/', api2.as_view(), name="basic user's APIs"),

    path('api3/', api3.as_view(), name="room management APIs"),
    path('api4/', api4.as_view(), name="meeting management APIs"),
]
