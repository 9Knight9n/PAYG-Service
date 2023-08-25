from django.contrib.auth import login
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from payg.utils import calculate_user_cost_current_month
from .serializers import AuthSerializer, UserSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(KnoxLoginView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        django_user = serializer.validated_data['user']
        login(request, django_user)
        response = super(LoginView, self).post(request, format=None)
        user = User.objects.get(user=django_user)
        response.data['username'] = django_user.username
        response.data['id'] = user.__dict__['id']
        del response.data['expiry']
        return response


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.get(user=request.user)
        return Response({
            'id': user.id,
            'username': str(user),
            'monthly_cost': calculate_user_cost_current_month(user),
            'total_cost': user.total_cost,
        })
