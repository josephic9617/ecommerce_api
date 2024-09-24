from django.urls import path
from main.views.category import CategoryView
from main.views.clothing import ClothingView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('clothings/', ClothingView.as_view()),
]