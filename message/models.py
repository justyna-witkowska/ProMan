from django.db import models
from django.db.models import ForeignKey

from accounts.models import Users


# Create your models here.


class Messages(models.Model):
    # user_from = ForeignKey(Profile, on_delete=models.DO_NOTHING)
    # user_to = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=1000)
    sent_date = models.DateField(auto_now_add=True)