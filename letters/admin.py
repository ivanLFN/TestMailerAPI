from django.contrib import admin
from letters.models import Client, Mailing, Message

admin.site.register(Client)
admin.site.register(Mailing)
admin.site.register(Message)

