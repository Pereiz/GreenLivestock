from django.db import models
from django.conf import settings

import uuid

# Create your models here.

class ModelParam(models.Model):
    """ModelParam est classe abstraite qui permet d'ajouter automatiquement ses attributs à toutes les classes dont elle est parente"""

    #UUIDField permet d'avoir des id sous forme de UUID
    id = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True, unique=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

### '%(class)s' est remplacé par le nom en minuscules de la classe enfant dans laquelle est utilisé le champ
#######Je dois recuperer l'utilisateur courant
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, related_name="created_%(class)s") 
    updated_by = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True, related_name="updated_%(class)s")
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class RoleUtilisateur(ModelParam):
    libelle = models.CharField(max_length=255, blank=False, null=False)

    
    def __str__(self) -> str:
        return self.libelle
    
    class Meta:
      db_table = ''
      managed = True
      verbose_name = 'Roles'
      verbose_name_plural = 'PRoles'

class Utilisateur(ModelParam):
    nom = models.CharField(max_length=255, blank=False, null=False)
    prenom = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    telephone = models.CharField(max_length=50, blank=False, null=False)
    adressePhysique = models.CharField(max_length=255, blank=False, null=False)
    longigtude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(to=RoleUtilisateur,on_delete=models.CASCADE, null=False, related_name="role_%(class)s")

    class Meta:
      ordering = ('-created_at',)
      managed = True
      verbose_name = 'Utilisateur'
      verbose_name_plural = 'Utilisateurs'

    def __str__(self) -> str:
        return "{} {}".format(self.nom, self.prenom)


class CategorieProduit(ModelParam):
    libelle = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
      return "{}".format(self.libelle)

    class Meta:
      db_table = ''
      managed = True
      verbose_name = 'CategorieProduit'
      verbose_name_plural = 'CategorieProduits'

class StatutStock(ModelParam):
    #" exemple : disponible, en stock, vendu etc"
    libelle = models.CharField(max_length=255, blank=False, null=False)
    

    def __str__(self):
      return "{}".format(self.libelle)

    class Meta:
      db_table = ''
      managed = True
      verbose_name = 'StatutStock'
      verbose_name_plural = 'StatutStocks'

class Produit(ModelParam):
    libelle = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.CharField(max_length=255, blank=False, null=False)
    categorie = models.ForeignKey(to=CategorieProduit,on_delete=models.CASCADE, null=False, related_name="categorie_%(class)s")
    statut = models.ForeignKey(to=StatutStock,on_delete=models.CASCADE, null=False, related_name="statut_%(class)s")

    quantitedispo = models.IntegerField()
    prix = models.PositiveIntegerField()

    def __str__(self):
      return "{}".format(self.libelle)

    class Meta:
      
      managed = True
      verbose_name = 'Produit'
      verbose_name_plural = 'Produits'

class StatutCommande(ModelParam):
    #" exemple : en attente, en cours de livraison, livrée, annulée etc"
    libelle = models.CharField(max_length=255, blank=False, null=False)
    

    def __str__(self):
      return "{}".format(self.libelle)

    class Meta:
      db_table = ''
      managed = True
      verbose_name = 'StatutCommande'
      verbose_name_plural = 'StatutCommandes'

class Commande(ModelParam):
    numero = models.PositiveIntegerField(unique=True, auto_created=True) #je pourrai écrire une fonction gerer le  numéro de la commande automatiquement
    commandeur = models.ForeignKey(to=Utilisateur,on_delete=models.CASCADE, null=False, related_name="commandeur_%(class)s")
    montant = models.PositiveIntegerField()


    def __str__(self):
      return "N°{} - {} - {}f".format(self.numero, self.commandeur, self.montant)

    class Meta:
      db_table = ''
      managed = True
      verbose_name = 'Commande'
      verbose_name_plural = 'Commandes'

class DetailCommande(ModelParam):
    commande = models.ForeignKey(to=Commande,on_delete=models.CASCADE, related_name="commande_%(class)s")
    produit = models.ForeignKey(to=Produit,on_delete=models.CASCADE, related_name="produit_%(class)s")
    quantite = models.PositiveIntegerField()
    prixcommande = models.PositiveIntegerField()
    

    def __str__(self):
      return "{} - {}".format(self.commande, self.produit)

    class Meta:
      db_table = ''
      managed = True
      verbose_name = 'DetailCommande'
      verbose_name_plural = 'DetailCommandes'

class AvisCommentaire(ModelParam):
  commentaire = models.TextField(blank=False, null=False)
  note = models.IntegerField() # je vais revenir faire un systeme d'echelle de 1 à 5
  produit = models.ForeignKey(to=Produit,on_delete=models.CASCADE, related_name="produit_%(class)s")
  utilisateur = models.ForeignKey(to=Utilisateur,on_delete=models.CASCADE, null=False, related_name="user_%(class)s")

  def __str__(self):
    return "{} - {}".format(self.utilisateur, self.commentaire)

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'AvisCommentaire'
    verbose_name_plural = 'AvisCommentaires'

class Favoris(ModelParam):
  #Je dois ajouter le champ utilisateur à cette table
  produit = models.ForeignKey(to=Produit,on_delete=models.CASCADE, related_name="produit_%(class)s")
  utilisateur = models.ForeignKey(to=Utilisateur,on_delete=models.CASCADE, null=False, related_name="user_%(class)s")


  def __str__(self):
    return "{} - {}".format(self.created_by, self.produit)

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Favoris'
    verbose_name_plural = 'Favoriss'
    

class StatutTransaction(ModelParam):
  #" exemple : réussie, en  attente, échouée"
  libelle = models.CharField(max_length=255, blank=False, null=False)
    

  def __str__(self):
    return self.libelle

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'StatutTransaction'
    verbose_name_plural = 'StatutTransactions'

class Transaction(ModelParam):
  numero = models.PositiveIntegerField(unique=True, auto_created=True) #je pourrai écrire une fonction gerer le  numéro de la commande automatiquement
  montant = models.PositiveIntegerField()
  utilisateur = models.ForeignKey(to=Utilisateur,on_delete=models.CASCADE, null=False, related_name="user_%(class)s")


  def __str__(self):
    return "N°{} - {} - {}f".format(self.numero, self.utilisateur, self.montant)

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Transaction'
    verbose_name_plural = 'Transactions'