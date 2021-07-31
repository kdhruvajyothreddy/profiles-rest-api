from django.contrib import admin
from profiles_api import models


# Register your models here.
# To register User Profile model with Admin site
admin.site.register(models.UserProfile)
