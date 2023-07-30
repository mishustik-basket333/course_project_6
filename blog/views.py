from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog
from clients.models import Mailings, Client


# Блоги
class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_flag=True, )
        return queryset


class BlogDetailView(DetailView):
    model = Blog


def home(request):
    mailings = Mailings.objects.all()
    clients = Client.objects.all()
    blogs = Blog.objects.filter(publication_flag=True).order_by('?')[:3]

    total_mailings = len(mailings) if len(mailings) > 0 else "ни одной рассылки"
    total__active_mailings = len(mailings.exclude(status='завершено')) \
        if len(mailings.exclude(status='завершено')) > 0 else "ни одной рассылки"
    total_clients = len(clients) if len(clients) > 0 else "ни одного клиента"

    context = {
        'count_all_mailings': total_mailings,
        'count_active_mailings': total__active_mailings,
        'count_clients': total_clients,
        'blogs': blogs,

    }
    return render(request, 'blog/home.html', context)
