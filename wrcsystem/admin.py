from django.contrib import admin
from .models import TestPost,WaterTemperature,WaterHigh,MapDanger
from .models import Account

admin.site.register(TestPost)
admin.site.register(WaterTemperature)
admin.site.register(WaterHigh)
admin.site.register(MapDanger)
admin.site.register(Account)