from django.urls import path

from django101.cities.views import index, list_phones, test_index, create_person
from django.views.generic import TemplateView

urlpatterns = [
    path('', index),
    path('create/', create_person, name="create person"),
    path('test/', test_index),
    path('phones/', list_phones),
    path('phones2/', TemplateView.as_view(template_name='phones.html')),
]
