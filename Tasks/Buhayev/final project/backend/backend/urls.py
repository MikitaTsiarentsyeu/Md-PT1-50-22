"""backend URL Configuration

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
from django.urls import path, include
from listings.api import views as listings_api_views
from users.api import views as users_api_views
from reviews.api import views as reviews_api_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/reviews/', reviews_api_views.ReviewList.as_view()),
    path('api/reviews/create/', reviews_api_views.ReviewCreate.as_view()),
    path('api/listings/', listings_api_views.ListingList.as_view()),
    path('api/listings/create/', listings_api_views.ListingCreate.as_view()),
    path('api/listings/<int:pk>/', listings_api_views.ListingDetail.as_view()),
    path('api/listings/<int:pk>/delete/', listings_api_views.ListingDelete.as_view()),
    path('api/listings/<int:pk>/update/', listings_api_views.ListingUpdate.as_view()),
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
    path('api/profiles/', users_api_views.ProfileList.as_view()),
    path('api/profiles/<int:seller>/', users_api_views.ProfileDetail.as_view()),
    path('api/profiles/<int:seller>/update/', users_api_views.ProfileUpdate.as_view()),
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
