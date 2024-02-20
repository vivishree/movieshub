
from django.contrib import admin
from django.urls import include, path
from . import views
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ad),
    path('in/',views.ad),
    path('about/',views.About),
    path('home/',views.home),
    path('pro/',views.proo),
    path('search/',views.ser),
    path('desc/',views.descp),
    path('stree/',views.stream),
    path('yaavarum/',views.yaa),
    path('nadi/',views.nadigayar),
    path('kalaa/',views.kala),
    path('sark/',views.sark),
    path('plus/', include('app1.urls')),
   

  
   
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
