from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from letters.models import Client, Message, Mailing
from letters.serializers import ClientSerializer, MessageSerializer, MailingSerializer
from rest_framework.response import Response
from letters.mailer import Mailer


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MailingListCreateView(generics.ListCreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

class MailingRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MailingStatisticsView(generics.RetrieveAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def get(self, request, *args, **kwargs):
        mailing = self.get_object()
        statistics = mailing.get_message_statistics()
        return Response(statistics)
    


def activate_mailing(request):
    # Создание экземпляра Mailer
    mailer = Mailer()
    mailer.process_active_mailings()

    mailing = Mailing.objects.get(id=2)
    statistics = mailing.get_message_statistics()
    print(statistics)

    # Получение клиента и рассылки
    # client = Client.objects.get(id=3)
    # mailing = Mailing.objects.get(id=2)

    # Отправка сообщения
    # message = mailer.send_message(client, mailing)
    # print(message)

    # if message.status == 'Отправлено':
    #     success_message = "Сообщение успешно отправлено"
    # else:
    #     success_message = "Ошибка отправки сообщения"
    success_message = "INTERGUIDE"

    return HttpResponse(success_message)

    # Дальнейшая обработка и отображение результата



