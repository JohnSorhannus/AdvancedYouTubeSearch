from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Video)
admin.site.register(Object)
#admin.site.register(VideoObject)