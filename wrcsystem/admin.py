from django.contrib import admin
from .models import TestPost
from .models import Account

admin.site.register(TestPost)
admin.site.register(Account)