from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import LogForm
from clients.models import Log


# Логи
#
class LogListView(ListView):
    model = Log


class LogDetailView(DetailView):
    model = Log

