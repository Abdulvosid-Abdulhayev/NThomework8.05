from django.urls import path
from .views import CategoryAPIView, FoodItemAPIView, OrderAPIView, CategoryDetailAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('food-items/', FoodItemAPIView.as_view(), name='food-items'),
    path('orders/', OrderAPIView.as_view(), name='orders'),
]
