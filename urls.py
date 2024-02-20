from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home2/',views.insert,name="insert"),
    path('home3/',views.insert1.as_view(),name="insert"),
    path('',views.Cr.as_view(),name="list"),
    path('delete/<int:pk>/', views.delete1.as_view(), name="delete1"),
    path('update/<int:pk>/', views.update1.as_view(), name="update1"),
    path('home/',views.HOME,name='home'),
    path('BASE1/',views.BASE1),
    path('signup/',views.Signup,name="signup"),
    path('logout/',views.Logout,name="logout"),
    path('log/',views.Login,name='log'),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
