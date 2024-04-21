from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Reivew)
class ReviewAdmin(admin.ModelAdmin):
    """Review Admin Definition"""

    pass
