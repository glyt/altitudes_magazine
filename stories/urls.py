from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='stories'),
    path('<int:story_id>', views.story, name='story'),
]