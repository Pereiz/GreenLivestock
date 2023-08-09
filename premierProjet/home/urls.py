from django.urls import path, include
from rest_framework import routers

from . import views



router = routers.SimpleRouter()

router.register('catprod',views.CategorieProduitViewSet, "Catégorie de Produit")
router.register("roleuser",views.RoleUserViewSet, basename="roleuser")
router.register("statutstock",views.StatutStockViewSet, basename="statutstock")
router.register("statutcommande",views.StatutCommandeViewSet, basename="statutcommande")
router.register("statuttransact",views.StatutTransactionViewSet, basename="statuttransact")
router.register("favoris",views.FavorisViewSet, basename="favoris")
router.register("produit",views.ProduitViewSet, basename="produit")
router.register("user",views.UtilisateurViewSet, basename="user")
router.register("commande",views.CommandeViewSet, basename="commande")
router.register("detailcommande",views.DetailcommandeViewSet, basename="detailcommande")
router.register("avis",views.AvisViewSet, basename="avis")
router.register("transaction",views.TransactionViewSet, basename="transaction")


#router.register("produit",views.ProduitViewSet, basename="produit")
app_name = 'gl'

urlpatterns = [
    #path("", views.index, name="index"),
    path("", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
]

# Inclure les URLs générées par le routeur dans la liste des URLs
#urlpatterns += router.urls