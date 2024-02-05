from django.shortcuts import render
from home.models import *
from home.serializers import (CategorieProduitListSerializer, CategorieProduitDetailSerializer,
                                RoleUserListSerializer, RoleUserDetailSerializer, StatutStockListSerializer,
                                StatutStockDetailSerializer,StatutCommandeListSerializer, StatutCommandeDetailSerializer,
                                StatutTransactionListSerializer, StatutTransactionDetailSerializer, FavorisListSerializer,
                                FavorisDetailSerializer, ProduitListSerializer, ProduitDetailSerializer,
                                UtilisateurListSerializer, UtilisateurDetailSerializer, CommandeListSerializer, 
                                CommandeDetailSerializer, DetailCommandeListSerializer, DetailCommandeDetailSerializer, 
                                AvisListSerializer, AvisDetailSerializer, TransactionListSerializer,
                                TransactionDetailSerializer,

                                )

from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
#def index(request):
#    return render(request, "home/base.html")


    


class CategorieProduitViewSet(viewsets.ModelViewSet):

    queryset = CategorieProduit.objects.all()

    # serializer_class = CategorieProduitSerializer
    # permission_classes = [] 
    
    
    def get_serializer_class(self):
        if self.action == "list":
            return CategorieProduitListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return CategorieProduitDetailSerializer
        else:
            return CategorieProduitDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = CategorieProduitListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorieProduitDetailSerializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorieProduitDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategorieProduitDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#"======================================================================================================="

class RoleUserViewSet(viewsets.ModelViewSet):
    queryset = RoleUtilisateur.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return RoleUserListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return RoleUserDetailSerializer
        else:
            return RoleUserDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = RoleUserListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RoleUserDetailSerializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RoleUserDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RoleUserDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
#"======================================================================================================="

class StatutStockViewSet(viewsets.ModelViewSet):
    queryset = StatutStock.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return StatutStockListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return StatutStockDetailSerializer
        else:
            return StatutStockDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = StatutStockListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutStockDetailSerializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutStockDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
        instance = self.get_object()
        serializer = StatutStockDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
#"======================================================================================================="

class StatutCommandeViewSet(viewsets.ModelViewSet):
    queryset = StatutCommande.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return StatutCommandeListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return StatutCommandeDetailSerializer
        else:
            return StatutCommandeDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = StatutCommandeListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutCommandeDetailSerializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutCommandeDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutCommandeDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#"======================================================================================================="

class StatutTransactionViewSet(viewsets.ModelViewSet):
    queryset = StatutTransaction.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return StatutTransactionListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return StatutTransactionDetailSerializer
        else:
            return StatutTransactionDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = StatutTransactionListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutTransactionDetailSerializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutTransactionDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatutTransactionDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#"======================================================================================================="

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProduitListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return ProduitDetailSerializer
        else:
            return ProduitDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = ProduitListSerializer(queryset, many=True)
        #data = serializer.data
        #print(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProduitDetailSerializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProduitDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer =ProduitDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#"======================================================================================================="

class FavorisViewSet(viewsets.ModelViewSet):
    queryset = Favoris.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return FavorisListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return FavorisDetailSerializer
        else:
            return FavorisDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = FavorisListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FavorisDetailSerializer(instance)
        #print(serializer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FavorisDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FavorisDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#"======================================================================================================="

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return UtilisateurListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return UtilisateurDetailSerializer
        else:
            return UtilisateurDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = UtilisateurListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UtilisateurDetailSerializer(instance)
        #print(serializer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UtilisateurDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UtilisateurDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


#"======================================================================================================="

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CommandeListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return CommandeDetailSerializer
        else:
            return CommandeDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = CommandeListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CommandeDetailSerializer(instance)
        #print(serializer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CommandeDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CommandeDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


#"======================================================================================================="

class DetailcommandeViewSet(viewsets.ModelViewSet):
    queryset = DetailCommande.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return DetailCommandeListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return DetailCommandeDetailSerializer
        else:
            return DetailCommandeDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = DetailCommandeListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DetailCommandeDetailSerializer(instance)
        #print(serializer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DetailCommandeDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DetailCommandeDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



#"======================================================================================================="

class AvisViewSet(viewsets.ModelViewSet):
    queryset = AvisCommentaire.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AvisListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return AvisDetailSerializer
        else:
            return AvisDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AvisListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer =AvisDetailSerializer(instance)
        #print(serializer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AvisDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AvisDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


#"======================================================================================================="

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TransactionListSerializer
        elif self.action in ["create","retrieve","update","partial_update"]:
            return TransactionDetailSerializer
        else:
            return TransactionDetailSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = TransactionListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer =TransactionDetailSerializer(instance)
        #print(serializer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TransactionDetailSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TransactionDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)