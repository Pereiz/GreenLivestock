from rest_framework import serializers
from .models import (Favoris, Produit, CategorieProduit, StatutCommande, StatutStock, StatutTransaction,
                    RoleUtilisateur, Utilisateur, Commande, DetailCommande, AvisCommentaire, Transaction, )


class CategorieProduitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieProduit
        fields = "__all__"
        #fields = ["id","libelle"]
        #exclude = [""]
    
    ####c'est ici que je peux ajouter des données au data de retour
    #### Je peux bien revenir dessus
    # def to_representation(self, instance):
    #     # Récupérer la représentation JSON par défaut
    #     data = super().to_representation(instance)
        
    #     # Ajouter des informations supplémentaires au format JSON
    #     data['custom_field'] = 'Valeur personnalisée'
        
    #     return data
class CategorieProduitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieProduit
        fields = ["libelle"]

#"======================================================================================================="

class RoleUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUtilisateur
        fields = "__all__"
class RoleUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUtilisateur
        fields = ["libelle"]
    

#"======================================================================================================="

class StatutStockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutStock
        fields = "__all__"
class StatutStockDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutStock
        fields = ["libelle"]

#"======================================================================================================="

class StatutCommandeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutCommande
        fields = "__all__"
class StatutCommandeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutCommande
        fields = ["libelle"]

#"======================================================================================================="

class StatutTransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutTransaction
        fields = "__all__"
class StatutTransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutTransaction
        fields = ["libelle"]

#"======================================================================================================="

class StatutTransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutTransaction
        fields = "__all__"
class StatutTransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutTransaction
        fields = ["libelle"]

#"======================================================================================================="

class ProduitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"

class ProduitDetailSerializer(serializers.ModelSerializer):
    categorie_libelle = serializers.SerializerMethodField()
    statut_libelle = serializers.SerializerMethodField()
    
    class Meta:
        model = Produit
        fields = ["libelle", "description", "categorie", "statut", "categorie_libelle","statut_libelle"]

    def get_categorie_libelle(self, obj):
        # Récupérez l'instance du categorie associé
        categorie_instance = obj.categorie

        # Sérialisez l'instance du produit pour obtenir le libellé
        categorie_serializer = CategorieProduitDetailSerializer(categorie_instance)
        return categorie_serializer.data['libelle']
    
    def get_statut_libelle(self, obj):
        # Récupérez l'instance du statut associé
        statut_instance = obj.statut

        # Sérialisez l'instance du produit pour obtenir le libellé
        statut_serializer = StatutStockDetailSerializer(statut_instance)
        return statut_serializer.data['libelle']




#"======================================================================================================="

class FavorisListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favoris
        fields = "__all__"

class FavorisDetailSerializer(serializers.ModelSerializer):
    produit_libelle = serializers.SerializerMethodField()
    produit_description = serializers.SerializerMethodField()
    utilisateur_nom = serializers.SerializerMethodField()

    class Meta:
        model = Favoris
        fields = ["produit", "produit_libelle","produit_description" , "utilisateur", "utilisateur_nom"]
    
    def get_produit_libelle(self, obj):
        # Récupérez l'instance du produit associé
        produit_instance = obj.produit

        # Sérialisez l'instance du produit pour obtenir le libellé
        produit_serializer = ProduitDetailSerializer(produit_instance)
        return produit_serializer.data['libelle']
    
    def get_produit_description(self, obj):
        # Récupérez l'instance du produit associé
        produit_instance = obj.produit

        # Sérialisez l'instance du produit pour obtenir la description
        produit_serializer = ProduitDetailSerializer(produit_instance)
        return produit_serializer.data['description']
    
    
    def get_utilisateur_nom(self, obj):
            # Récupérez l'instance du utilisateur associé
            utilisateur_instance = obj.utilisateur

            # Sérialisez l'instance du commandeur pour obtenir le nom
            utilisateur_serializer = UtilisateurDetailSerializer(utilisateur_instance)
            return utilisateur_serializer.data['nom']

#"======================================================================================================="

class UtilisateurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = "__all__"
class UtilisateurDetailSerializer(serializers.ModelSerializer):
    role_libelle = serializers.SerializerMethodField()
    class Meta:
        model = Utilisateur
        fields = ["nom", "prenom", "email", "telephone", "adressePhysique", "longigtude", "latitude", "role", "role_libelle"]
    
    def get_role_libelle(self, obj):
        # Récupérez l'instance du role associé
        role_instance = obj.role

        # Sérialisez l'instance du role pour obtenir le libellé
        role_serializer = ProduitDetailSerializer(role_instance)
        return role_serializer.data['libelle']


#"======================================================================================================="

class CommandeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = "__all__"

class CommandeDetailSerializer(serializers.ModelSerializer):
    commandeur_nom = serializers.SerializerMethodField()
    commandeur_prenom = serializers.SerializerMethodField()

    class Meta:
        model = Commande
        fields = ["numero", "commandeur","commandeur_nom","commandeur_prenom", "montant"]
    
    def get_commandeur_nom(self, obj):
        # Récupérez l'instance du commandeur associé
        commandeur_instance = obj.commandeur

        # Sérialisez l'instance du commandeur pour obtenir le nom
        commandeur_serializer = UtilisateurDetailSerializer(commandeur_instance)
        return commandeur_serializer.data['nom']
    
    def get_commandeur_prenom(self, obj):
        # Récupérez l'instance du commandeur associé
        commandeur_instance = obj.role

        # Sérialisez l'instance du commandeur pour obtenir le prenom
        commandeur_serializer = UtilisateurDetailSerializer(commandeur_instance)
        return commandeur_serializer.data['prenom']


#"======================================================================================================="

class DetailCommandeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCommande
        fields = "__all__"

class DetailCommandeDetailSerializer(serializers.ModelSerializer):
    # commandeur_nom = serializers.SerializerMethodField()
    # commandeur_prenom = serializers.SerializerMethodField()

    class Meta:
        model = DetailCommande
        fields = ["commande", "produit", "quantite", "prixcommande"]
    
    # def get_commandeur_nom(self, obj):
    #     # Récupérez l'instance du commandeur associé
    #     commandeur_instance = obj.role

    #     # Sérialisez l'instance du commandeur pour obtenir le nom
    #     commandeur_serializer = UtilisateurDetailSerializer(commandeur_instance)
    #     return commandeur_serializer.data['nom']



#"======================================================================================================="

class AvisListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvisCommentaire
        fields = "__all__"

class AvisDetailSerializer(serializers.ModelSerializer):
    utilisateur_nom = serializers.SerializerMethodField()
    produit_libelle = serializers.SerializerMethodField()

    class Meta:
        model = AvisCommentaire
        fields = ["commentaire", "note", "produit", "utilisateur", "utilisateur_nom", "produit_libelle"]
    
    def get_utilisateur_nom(self, obj):
        # Récupérez l'instance du utilisateur associé
        utilisateur_instance = obj.utilisateur

        # Sérialisez l'instance du commandeur pour obtenir le nom
        utilisateur_serializer = UtilisateurDetailSerializer(utilisateur_instance)
        return utilisateur_serializer.data['nom']
    
    def get_produit_libelle(self, obj):
        # Récupérez l'instance du produit associé
        produit_instance = obj.produit

        # Sérialisez l'instance du produit pour obtenir le libellé
        produit_serializer = ProduitDetailSerializer(produit_instance)
        return produit_serializer.data['libelle']




#"======================================================================================================="

class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

class TransactionDetailSerializer(serializers.ModelSerializer):
    utilisateur_nom = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ["numero", "utilisateur", "utilisateur_nom", "montant"]
    
    def get_utilisateur_nom(self, obj):
        # Récupérez l'instance du utilisateur associé
        utilisateur_instance = obj.utilisateur

        # Sérialisez l'instance du commandeur pour obtenir le nom
        utilisateur_serializer = UtilisateurDetailSerializer(utilisateur_instance)
        return utilisateur_serializer.data['nom']
    
