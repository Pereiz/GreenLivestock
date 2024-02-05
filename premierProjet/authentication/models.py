from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager,PermissionsMixin, Group, Permission)

from home.models import RoleUtilisateur, ModelParam

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None,**kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
           **kwargs
        )        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username,password,**kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            **kwargs
        
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin,ModelParam):
    username = models.CharField(max_length=255,null=False,db_index=True)
    email = models.EmailField(verbose_name="Adresse Email",null=False, unique=True,db_index=True,db_column='email')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #password = models.CharField(max_length=255, blank=False, null=False)
    addresse = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to="users_images",default="static/images/default_user.png")
    longigtude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(to=RoleUtilisateur,on_delete=models.CASCADE, null=False, related_name="role_%(class)s")

    is_admin = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)   
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permission_set')
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name','address','phone','image']

    class Meta:
      ordering = ('-created_at',)
      managed = True
      verbose_name = 'User'
      verbose_name_plural = 'Users'

    objects = UserManager() 
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
            return self.is_admin
    
    def get_short_name(self):
        return self.username
    
    
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'
    
    def has_module_perms(self, app_label) :
        return True


class UserActivationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activation_code = models.CharField(max_length=20, null=True)
    usable = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.email + " : " + self.activation_code
    
