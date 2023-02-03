from django.urls import path

from webapp.views import indexview

app_name = 'webapp'


urlpatterns = [
    path('', indexview, name='index_view'),
]
