from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import MailingsForm
from clients.models import Mailings


# Сообщения
#
class MailingsUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy("users:login")


class MailingsCreateView(LoginRequiredMixin, CreateView):
    model = Mailings
    form_class = MailingsForm
    success_url = reverse_lazy("users:login")


class MailingsListView(LoginRequiredMixin, ListView):
    model = Mailings


class MailingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mailings
    success_url = reverse_lazy("users:login")
    permission_required = 'mailings.delete_client'


class MailingsDetailView(LoginRequiredMixin, DetailView):
    model = Mailings
