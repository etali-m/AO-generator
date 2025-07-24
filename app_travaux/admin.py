from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

# Register your models here.
admin.site.register(AvisAppelOffre)
class AvisAppelOffreAdmin(TranslationAdmin):
    pass

admin.site.register(RPAO)
admin.site.register(CCAP) 
admin.site.register(CCTP)
admin.site.register(BPU)
admin.site.register(DQE)
admin.site.register(ModelMarche) 