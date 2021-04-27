from django.contrib import admin
from .models import (
    MessageAction,
    ThreadMember,
    Thread,
    Message,
    ThreadAction,
    ForwardedMessage,
)

admin.site.register(ForwardedMessage)
admin.site.register(Thread)
admin.site.register(ThreadMember)
admin.site.register(MessageAction)
admin.site.register(ThreadAction)
admin.site.register(Message)

# Register your models here.
