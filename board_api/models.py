import dateutil.utils
from django.db import models
from django.conf import settings

class board_api(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) #primary key
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add : '객체를 하나 생성할 때만 시간을 담겠다' 라는 의미
    updated_at = models.DateTimeField(auto_now=True)  # auto_now : 지금 작업을 할 때
