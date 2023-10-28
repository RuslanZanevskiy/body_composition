from django.urls import path

from . import views


urlpatterns = [
    path('add/', views.FoodCreateView.as_view(), name='food_create'),
    path('all/', views.FoodListView.as_view(), name='food_list'),
    path('delete/', views.FoodDeleteView.as_view(), name='food_delete'),
    path('update/', views.FoodUpdateView.as_view(), name='food_update'),
    path('<int:pk>/', views.FoodDetailView.as_view(), name='food_detail'),
]
