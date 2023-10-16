from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class CustomUserManager(BaseUserManager):
    def create_user(self,email, password=None, **extra_fields):
        if not email:
            raise ValueError('O Email é obrigatório!')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    
    

    def create_superuser(self,email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuários devem ter is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuários devem ter is_superuser=True')
        
        return self.create_user(email,password,**extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email=email)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    objects = CustomUserManager()

    def __str__ (self):
        return self.email
    


   

