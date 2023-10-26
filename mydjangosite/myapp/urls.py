"""
URL configuration for mydjangosite project.

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_thuephong', views.add_thuephong, name='add_thuephong'),
    path('add_product', views.add_product, name='add_product'),
    path('product_list', views.product_list, name='product_list'),
    path('list_rooms', views.list_rooms, name='list_rooms'),
    path('', views.homee, name='homee'),
    path('add_producta', views.add_producta, name='add_producta'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('add_thuephong/<int:maPhong>/', views.add_thuephong, name='add_thuephong'),
    path('savethuephong/<int:maPhong>/', views.savethuephong, name='savethuephong'),
    path('savedatphongphong/<int:maPhong>/', views.savedatphongphong, name='savedatphongphong'),
    path('view_thue_phong/<int:maPhong>/', views.view_thue_phong, name='view_thue_phong'),
    path('delete_thue_dich_vu/<int:maThueDichVu>/<int:maPhong>/', views.delete_thue_dich_vu,
         name='delete_thue_dich_vu'),
    path('update_thue_dich_vu/<int:maThueDichVu>/<int:maPhong>/', views.update_thue_dich_vu,
         name='update_thue_dich_vu'),
    path('add_thue_dich_vu', views.add_thue_dich_vu, name='add_thue_dich_vu'),
    path('login', views.login, name='login'),
    path('process_login', views.process_login, name='process_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('add_traphong', views.add_traphong, name='add_traphong'),
    path('don_phong/<int:maPhong>/', views.don_phong, name='don_phong'),
    path('nhan_phong/<int:maPhong>/', views.nhan_phong, name='nhan_phong'),
    path('addnhanphong', views.addnhanphong, name='addnhanphong'),

]
