from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AppelOffre, StatutPiece, Piece

@receiver(post_save, sender=AppelOffre)
def create_statut_pieces(sender, instance, created, **kwargs):
    if created:
        pieces = Piece.objects.filter(type_marche=instance.type_marche)
        for piece in pieces:
            StatutPiece.objects.create(
                appel_offre=instance,
                piece=piece,
                is_complete=piece.statut  # On copie la valeur du statut par défaut
            )
