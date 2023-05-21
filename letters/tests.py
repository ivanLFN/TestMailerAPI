from datetime import timedelta, timezone
import json
from django.test import TestCase
import requests
from letters.models import Client, Message, Mailing
from letters.serializers import ClientSerializer, MailingSerializer, MessageSerializer
from rest_framework.test import APITestCase


class ModelTest(TestCase):

    def setUp(self):
        self.client_obj = Client.objects.create(
            phone_number="12345678901",
            operator_code="001",
            tag="test_tag",
            timezone="UTC"
        )
        self.mailing_obj = Mailing.objects.create(
            start_datetime=timezone.now(),
            end_datetime=timezone.now() + timedelta(days=1),
            message_text="Hello, this is a test message.",
            filter_operator_code="001",
            filter_tag="test_tag"
        )

    def test_model_client(self):
        self.assertEqual(str(self.client_obj), "12345678901")

    def test_model_message(self):
        message_obj = Message.objects.create(
            mailing=self.mailing_obj,
            client=self.client_obj,
            status="Отправлено"
        )
        self.assertEqual(str(message_obj), str(message_obj.id))


    
class ClientSerializerTestCase(APITestCase):

    def setUp(self):
        self.client_data = {
            "phone_number": "1234567890",
            "operator_code": "001",
            "tag": "test",
            "timezone": "UTC"
        }

        self.client_obj = Client.objects.create(**self.client_data)

    def test_client_serializer(self):
        serializer = ClientSerializer(self.client_obj)
        self.assertEqual(serializer.data, self.client_data)

    def test_client_deserializer(self):
        serializer = ClientSerializer(data=self.client_data)
        self.assertEqual(serializer.is_valid())

    def test_client_deserializer_invalid(self):
        invalid_client_data = self.client_data.copy()
        invalid_client_data["phone_number"] = ''
        serializer = ClientSerializer(data=invalid_client_data)
        self.assertEqual(serializer.is_valid())






# url = 'http://127.0.0.1:8000/clients/'

# data = {
#     "phone_number": "90000000000",
#     "operator_code": "913",
#     "tag": "new_client",
#     "timezone": "GMT+3"
# }

# headers = {'Content-Type': 'application/json'}

# response = requests.post(url, data=json.dumps(data), headers=headers)
# print(response.text)


# url = 'http://127.0.0.1:8000/clients/2/'    

# data = {
#     "phone_number": "71234567890",
#     "operator_code": "456",
#     "tag": "updated_client",
#     "timezone": "GMT+4"
# }

# headers = {'Content-Type': 'application/json'}

# response = requests.put(url, data=json.dumps(data), headers=headers)
# print(response.text)


# url = 'http://127.0.0.1:8000/clients/2/'    

# response = requests.delete(url)
# print(response.text)

# url = 'http://127.0.0.1:8000/mailings/' 

# data = {
#     "start_datetime": "2023-05-18T09:00:00",
#     "message_text": "Third mailing!",
#     "filter_operator_code": "913",
#     "filter_tag": "new_client",
#     "end_datetime": "2023-05-25T18:00:00"
# }

# headers = {'Content-Type': 'application/json'}

# response = requests.post(url, data=json.dumps(data), headers=headers)
# print(response.text)





# for mailing in Mailing.objects.all():
#     url = f'http://127.0.0.1:8000/mailings/{mailing.id}/statistics/'
#     response = requests.get(url)
#     print(response.text)









