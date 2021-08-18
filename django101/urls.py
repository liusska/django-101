from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('django101.cities.urls')),
    path('people/', include('django101.people.urls')),
]
