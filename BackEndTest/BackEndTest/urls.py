from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Powtoon import views as powtoonviewsets
from Share import views as shareViewSets


route = routers.DefaultRouter()
route.register(r'powtoon',powtoonviewsets.PowtoonViewSet, basename ="Powtoon")
route.register(r'share',shareViewSets.SharePowtoonViewSet, basename ="SharePowtoon")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path(r'',include(route.urls)),
]
