from django.contrib import admin
from Main.models import Contact



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','datetime')

