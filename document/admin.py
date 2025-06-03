from django.contrib import admin
from .models import TypeMarche, AppelOffre, Piece, StatutPiece

# Register your models here.
admin.site.register(TypeMarche)
admin.site.register(Piece)
admin.site.register(AppelOffre)
admin.site.register(StatutPiece)
