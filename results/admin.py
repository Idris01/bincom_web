from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Agentname)
class AgentnameAdmin(admin.ModelAdmin):
    pass

@admin.register(AnnouncedLgaResults)
class AnnouncedLgaAdmin(admin.ModelAdmin):
    pass

@admin.register(AnnouncedPuResults)
class AnnouncedPuAdmin(admin.ModelAdmin):
    pass

@admin.register(AnnouncedStateResults)
class AnnouncedStateAdmin(admin.ModelAdmin):
    pass

@admin.register(AnnouncedWardResults)
class AnnouncedWardAdmin(admin.ModelAdmin):
    pass

@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Lga)
class LgaAdmin(admin.ModelAdmin):
    pass