from django.contrib import admin

from login import models

admin.site.register(models.User)
admin.site.register(models.ConfirmString)
