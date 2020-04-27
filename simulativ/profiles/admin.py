from django.contrib import admin
from . import models

profileModels = [models.Profile, models.ProfileStatus]

admin.site.register(profileModels)
