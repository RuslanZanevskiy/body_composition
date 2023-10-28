from django.shortcuts import render
from django.views import generic

from .models import Food


class FoodCreateView(generic.CreateView):
    model = Food

class FoodDetailView(generic.DetailView):
    model = Food
    template_name = 'food_stats/food_list.html'

class FoodListView(generic.ListView):
    model = Food

class FoodUpdateView(generic.UpdateView):
    model = Food

class FoodDeleteView(generic.DeleteView):
    model = Food