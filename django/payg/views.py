import json
from datetime import datetime
from random import randrange
import requests
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class Api1(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            res = requests.get('https://www.boredapi.com/api/activity', timeout=2.50).json()
        except:
            res = {'result': f"failed to fetch a random activity. here is current time instead: {datetime.now()} :)"}
        return Response(
            res,
            status=status.HTTP_200_OK
        )


class Api2(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            res = requests.get('https://api.quotable.io/quotes/random', timeout=2.50).json()
        except:
            res = {'result': f"failed to fetch a random quote. here is current time instead: {datetime.now()} :)"}
        return Response(
            res,
            status=status.HTTP_200_OK
        )

class Api3(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            res = requests.get(f'https://rickandmortyapi.com/api/character/{randrange(826)+1}', timeout=2.50).json()
        except:
            res = {'result': f"failed to fetch a random Rick and Morty character. "
                             f"here is current time instead: {datetime.now()} :)"}
        return Response(
            res,
            status=status.HTTP_200_OK
        )
