from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import MailForm
from clients.models import Mail


# Сообщения
#
class MailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy("users:login")


class MailCreateView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy("users:login")


class MailDeleteView(UserPassesTestMixin, DeleteView):
    model = Mail
    success_url = reverse_lazy("users:login")
    permission_required = 'client.delete_client'


class MailListView(LoginRequiredMixin, ListView):
    model = Mail
    success_url = reverse_lazy("blog:blogs_list")


class MailDetailView(LoginRequiredMixin, DetailView):
    model = Mail

