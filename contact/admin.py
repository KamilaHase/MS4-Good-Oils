from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Renders Models to the Admin View"""

    list_display = (
        'date_sent',
        'subject',
        'name',
        'email',
        'message',
    )

    readonly_fields = (
        'date_sent',
    )

    ordering = ('date_sent',)


admin.site.register(Contact, ContactAdmin)
