from django.core.validators import MinValueValidator
from django.db import models
import uuid
from django.contrib.auth.models import User as DjangoUser
from django.db.models import F


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(DjangoUser, on_delete=models.DO_NOTHING, null=False, blank=False)
    total_cost = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)], null=False, blank=False)

    def __str__(self):
        return self.user.username

    def increase_count(self, new_cost):
        self.total_cost = F('total_cost') + new_cost
        self.save()
