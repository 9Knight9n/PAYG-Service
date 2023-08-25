from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import F
from authentication.models import User


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False)
    api = models.CharField(max_length=1024, null=False, blank=False)
    method = models.CharField(max_length=10)
    month = models.PositiveSmallIntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)],
                                             null=False, blank=False)
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), MinValueValidator(1950)],
                                            null=False, blank=False)
    count = models.PositiveIntegerField(default=0, null=False, blank=False)

    class Meta:
        unique_together = ['user', 'api', 'month', 'year', 'method']

    @property
    def date(self):
        return f"{self.year}/{self.month}"

    def __str__(self):
        return f"{self.user}#{self.method}#{self.api}#{self.date} => {self.count}"

    def increase_count(self):
        self.count = F('count') + 1
        self.save()


