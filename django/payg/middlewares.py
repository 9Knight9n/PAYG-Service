from datetime import datetime
from django.urls import resolve
from authentication.models import User
from payg.config import LOGGER_ALLOWED_NAMESPACES, LOGGER_ALLOWED_STATUS_CODES
from payg.models import Record


class APILoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.LOGGER_ALLOWED_NAMESPACES = LOGGER_ALLOWED_NAMESPACES
        self.LOGGER_ALLOWED_STATUS_CODES = LOGGER_ALLOWED_STATUS_CODES

    def __call__(self, request):
        # skipping non pay-as-you-go APIs
        namespace = resolve(request.path_info).namespace
        if namespace not in self.LOGGER_ALLOWED_NAMESPACES:
            return self.get_response(request)

        # running view
        response = self.get_response(request)

        # Only log allowed status codes
        if response.status_code not in self.LOGGER_ALLOWED_STATUS_CODES:
            return response

        api = request.path
        method = request.method
        date = datetime.now()

        obj, _ = Record.objects.get_or_create(
            user=User.objects.get(user=request.user),
            api=api,
            method=method,
            month=date.month,
            year=date.year,
        )
        obj.increase_count()
        return response
