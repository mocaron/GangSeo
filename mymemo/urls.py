from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('create/', views.create),
    path('edit/<str:idx>', views.editPage),
    path('edit/update/', views.updateMemo),
]
