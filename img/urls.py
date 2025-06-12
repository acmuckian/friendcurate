from . import views
from django.urls import path

urlpatterns = [
    path('', views.ImgList.as_view(), name='home'),
    path('<slug:slug>/', views.img_detail, name="img_detail")
]