
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('venta/', include('venta.urls')),
    
    path('apix/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apix/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
