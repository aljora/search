from . import views
from django.views.generic import TemplateView
from django.urls import path

app_name = 'movie'
urlpatterns = [
    path('', TemplateView.as_view(template_name='movie/index.html'), name='index'),
    path('search/', views.search, name='search'),
]
