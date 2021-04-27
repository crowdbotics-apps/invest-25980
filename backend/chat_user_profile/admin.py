from django.contrib import admin
from .models import Profile, VerificationCode, Contact

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(VerificationCode)

# Register your models here.
