from django.contrib import admin
from .models import TestPost,WaterTemperature
from .models import Account

admin.site.register(TestPost)
admin.site.register(WaterTemperature)
admin.site.register(Account)