from django.contrib import admin
from .models import Writer, Publication, Subject

admin.site.register(Writer)
admin.site.register(Publication)
admin.site.register(Subject)
