from django.urls import path
from . import views

urlpatterns = [
    		
            path('cadastro',views.create_user, name='cadastro'),
            path('entrar', views.entrar, name='entrar'),
            

	    ]