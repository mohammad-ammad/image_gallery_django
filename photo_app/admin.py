from django.contrib import admin
from .models.upload import Upload
from .models.useraccount import Useraccount
# Register your models here.
admin.site.register(Upload)
admin.site.register(Useraccount)