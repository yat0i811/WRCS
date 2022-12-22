from django.contrib import admin

# Register your models here.
from .models import WRCS_samples,WebLayoutQuestions

admin.site.register(WRCS_samples)
admin.site.register(WebLayoutQuestions)