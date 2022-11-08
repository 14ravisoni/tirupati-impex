"""tirupati_impex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register('workers', views.WorkerViewSet)
router.register('jewl-types', views.JewlTypeViewSet)
router.register('jewl-stages', views.JewlStageViewSet)
router.register('jewls', views.JewlViewSet)
router.register('stones', views.StoneViewSet)
router.register('stone-transaction', views.StoneJadaiTransactionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('metal/', views.credit_debit_metal),
    path('current-metal-stock/', views.get_current_metal_stock),
    path('current-all-jewl-count/', views.get_all_current_jewl_count),
    path('jewl-stage/', views.JewlRetrieve.as_view()),
    path('jewl-ghaat/', views.JewlGhaatAddition.as_view()),
    path('jewl-jadai/', views.JewlJadaiAddition.as_view()),
]
