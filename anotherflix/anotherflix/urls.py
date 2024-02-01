from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Endpoint para obter token
    path('api/', include('games.urls')),  # Inclui as URLs do app 'games'
]