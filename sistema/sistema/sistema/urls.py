from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout, LoginAPI

urlpatterns = [
    path('autenticacao-api/', LoginAPI.as_view()),
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('camisa/', include('camisa.urls')),
    path('anuncio/', include('anuncio.urls'), name='anuncio'),
    
    
]
