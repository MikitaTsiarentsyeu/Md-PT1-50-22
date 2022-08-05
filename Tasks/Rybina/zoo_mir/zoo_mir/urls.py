"""zoo_mir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from main_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path('cart/', include('cart.urls')),
    path('cart/', views.cart_detail, name='cart_detail'), 
    path('cart/add/<product_id>', views.cart_add, name='cart_add'),
    path('cart/remove/<product_id>', views.cart_remove, name='cart_remove'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/<int:category_id>', views.category_products, name='category'),
    path('category/<str:category_id>', views.category_products, name='category'),
    path('products/', views.product_list, name='products'),
    path('product/<int:product_id>', views.product_details, name='product'),
    path('product/<str:product_id>', views.product_details, name='product'),
    path('', views.home, name='home'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)