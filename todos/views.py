from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import redirect
from datetime import date
from django.shortcuts import get_object_or_404, redirect
from .models import Todo

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','deadline']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')
