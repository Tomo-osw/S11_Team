from django.contrib import admin

from .models import Account
from .models import Lists

admin.site.register(Account)
admin.site.register(Lists)
