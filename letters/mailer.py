from django.utils import timezone
import requests
from letters.models import Client, Message, Mailing
from requests.exceptions import ConnectionError

class Mailer:
    def select_clients(self, filter_properties):
        clients = Client.objects.filter(**filter_properties)
        return clients
    

    def send_message(self, client, mailing):
        try:
            token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU5NjM0MTIsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9JdmFuX0xvemhraW4ifQ.-hfJVgttn7SQsXuAeutlL0FCeTdqwWiHN30IIGFdq9s"
            base_url = "https://probe.fbrq.cloud/v1"
            endpoint = f"/send/{client.id}"

            url = base_url + endpoint

            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }

            data = {
                "id": (client.id),
                "phone": client.phone_number,
                "text": mailing.message_text
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                # Обработка успешного ответа
                response_data = response.json()
                print(response_data)
                
                Message.objects.create(
                    client=client,
                    mailing=mailing,
                    status="Отправлено",
                    created_at=timezone.now()
                )
                
            else:
                # Обработка ошибки запроса
                print('400')
        except ConnectionError as e:
            # Обработка ошибки соединения
            print(f"Ошибка соединения: {str(e)}")



    def process_active_mailings(self):

        current_time = timezone.now()

        active_mailings = Mailing.objects.filter(start_datetime__lte=current_time)

        for mailing in active_mailings:
            if current_time <= mailing.end_datetime:

                filter_properties = {
                    'operator_code': mailing.filter_operator_code,
                    'tag': mailing.filter_tag
                }
                clients = self.select_clients(filter_properties)

                for client in clients:
                        # Отправка сообщения каждому клиенту
                        self.send_message(client, mailing)

            else:
                # Если текущее время выходит за границы времени окончания рассылки,
                # обновляем статус рассылки на "Завершено"
                mailing.status = "Завершено"
                mailing.save()