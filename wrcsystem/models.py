from venv import create
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TestPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class WaterTemperature(models.Model):
    RaspberryPi_Name = models.CharField(max_length=16)
    celsius = models.DecimalField(max_digits=5,decimal_places=3) #摂氏温度
    fahrenheit = models.DecimalField(max_digits=5,decimal_places=3) #華氏温度
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.RaspberryPi_Name

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username