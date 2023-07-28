from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogListView, BlogDetailView, home

app_name = 'blog'

urlpatterns = [

    path('blogs/', cache_page(60)(BlogListView.as_view()), name='blogs_list'),
    path('blog/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog'),
    path('', cache_page(60)(home), name='home'),

]
