from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, unique=True)
    operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.phone_number)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)
    

class Mailing(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    message_text = models.TextField()
    filter_operator_code = models.CharField(max_length=3, blank=True, null=True)
    filter_tag = models.CharField(max_length=255, blank=True, null=True)

    def get_message_statistics(self):
        return self.message_set.values('status').annotate(count=models.Count('status'))
    