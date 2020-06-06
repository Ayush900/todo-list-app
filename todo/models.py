from django.db import models
from django.contrib.auth.models import User

class todoslist(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    datecompleted = models.DateTimeField(null = True ,blank = True)
    important = models.BooleanField(default = False)
    user = models.ForeignKey(User,models.SET_NULL,null=True)

    def __str__(self):
        return self.title
