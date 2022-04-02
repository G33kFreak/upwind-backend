from django.contrib import admin
from django.urls import path, include

from users.urls import auth_urls

api_urls = [
    path('', include('users.urls')),
    path('', include('habits.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('', include('jwt_auth.urls')),
    path('auth/', include(auth_urls)),
]
