from django.urls import path
from payg.views import Api1, Api2, Api3

app_name = "payg"
urlpatterns = [
    path('api1/', Api1.as_view(), name="get a random activity suggestion "
                                       "or current time if external API not available"),
    path('api2/', Api2.as_view(), name="get a random quote or current time if external API not available"),
    path('api3/', Api3.as_view(), name="get a random Rick and Morty character or "
                                       "current time if external API not available"),
]
