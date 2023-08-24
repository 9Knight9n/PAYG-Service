from django.db import models
import uuid
from django.contrib.auth.models import User as DjangoUser


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(DjangoUser, on_delete=models.DO_NOTHING, null=False, blank=False)

    def __str__(self):
        return self.user.username
