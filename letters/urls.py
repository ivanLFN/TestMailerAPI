from django.urls import path
from django.urls import path
from letters.views import (
    ClientListCreateView,
    ClientRetrieveUpdateDeleteView,
    MailingListCreateView,
    MailingRetrieveUpdateDeleteView,
    MessageListCreateView,
    MessageRetrieveUpdateDeleteView,
    MailingStatisticsView,
    activate_mailing
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDeleteView.as_view(), name='client-retrieve-update-delete'),
    path('mailings/', MailingListCreateView.as_view(), name='mailing-list-create'),
    path('mailings/<int:pk>/', MailingRetrieveUpdateDeleteView.as_view(), name='mailing-retrieve-update-delete'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDeleteView.as_view(), name='message-retrieve-update-delete'),
    path('mailings/<int:pk>/statistics/', MailingStatisticsView.as_view(), name='mailing-statistics'),

    path('activate-mailing/', activate_mailing, name='activate_mailing'),
]

