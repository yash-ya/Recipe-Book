from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('app/', include('recipe_list.urls')),
    path('admin/', admin.site.urls),
]
