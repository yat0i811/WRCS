from django.contrib import admin
from .models import TestPost,OldWaterTemperature,OldWaterHigh,MapDanger,WRCSAll
from .models import Account

admin.site.register(WRCSAll)
admin.site.register(TestPost)
admin.site.register(OldWaterTemperature)
admin.site.register(OldWaterHigh)
admin.site.register(MapDanger)
admin.site.register(Account)