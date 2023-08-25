from django.urls import path
from knox import views as knox_views
from .views import RegisterView, LoginView, UserView

app_name = "authentication"
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('info/', UserView.as_view(), name="user info containing username, id and current month cost"),
]
