from . import views
from django.urls import path

urlpatterns = [
    path('', views.ImgList.as_view(), name='home'),
    path('fav/<int:id>/', views.add_favourite, name='add_favourite'),
    path('favourites/', views.my_favourites, name="my_favourites"),
    path('<slug:slug>/', views.img_detail, name="img_detail"),
]