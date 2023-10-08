
from django.urls import path
from service.apps import ServiceConfig
from service.views import IndexView, ClientListView, MailingListView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView, MailingDetailView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MessageDetailView, LogsListView

app_name = ServiceConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/', ClientListView.as_view(), name='client'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('clients/edit/<int:pk>/', ClientDetailView.as_view(), name='client_edit'),
    path('mailings/', MailingListView.as_view(), name='mailing'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailings/edit/<int:pk>/', MailingDetailView.as_view(), name='mailing_edit'),
    path('message/', MessageListView.as_view(), name='message'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('message/edit/<int:pk>', MessageDetailView.as_view(), name='message_edit'),
    path('logs/', LogsListView.as_view(), name='logs'),
]
