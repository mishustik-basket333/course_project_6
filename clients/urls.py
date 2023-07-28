from django.urls import path

from clients.views.client import ClientCreateView, ClientUpdateView, ClientDeleteView, ClientsListView, ClientDetailView
from clients.views.log import LogListView, LogDetailView
from clients.views.mail import MailCreateView, MailUpdateView, MailListView, MailDetailView, MailDeleteView
from clients.views.mailing import MailingsCreateView, MailingsUpdateView, MailingsListView, MailingsDeleteView, MailingsDetailView

app_name = 'clients'

urlpatterns = [

    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/', ClientsListView.as_view(), name='clients_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('mail/create', MailCreateView.as_view(), name='mail_create'),
    path('mail/update/<int:pk>/', MailUpdateView.as_view(), name='mail_update'),
    path('mails/', MailListView.as_view(), name='mail_list'),
    path('mail/<int:pk>/', MailDetailView.as_view(), name='mail'),
    path('mail/delete/<int:pk>', MailDeleteView.as_view(), name='mail_delete'),

    path('mailing/create', MailingsCreateView.as_view(), name='mailing_create'),
    path('mailings/', MailingsListView.as_view(), name='mailings_list'),
    path('mailing/<int:pk>/', MailingsDetailView.as_view(), name='mailing'),
    path('mailing/update/<int:pk>/', MailingsUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>', MailingsDeleteView.as_view(), name='mailing_delete'),

    path('logs/', LogListView.as_view(), name='logs_list'),
    path('log/<int:pk>/', LogDetailView.as_view(), name='log'),


]
