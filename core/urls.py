from django.contrib import admin
from django.urls import path, include
from api.urls import router as router_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_api.urls)),
]
