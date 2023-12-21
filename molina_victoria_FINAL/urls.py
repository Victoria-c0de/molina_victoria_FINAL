"""
URL configuration for molina_victoria_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# molina_victoria_FINAL/urls.py
from django.urls import path
from seminario.views import InscritoListCreateView, InscritoDetailView, inscrito_list, inscrito_detail, index, get_autor_info

urlpatterns = [
    path('', index, name='index'),  # Página principal
    path('api/inscritos/', InscritoListCreateView.as_view(), name='inscrito-list-create'),
    path('api/inscritos/<int:id>/', InscritoDetailView.as_view(), name='inscrito-detail'),
    path('api/inscritos/', inscrito_list, name='inscrito-list-fbv'),
    path('api/inscritos/<int:id>/', inscrito_detail, name='inscrito-detail-fbv'),
    path('api/autor/', get_autor_info, name='get-autor-info'),

]
