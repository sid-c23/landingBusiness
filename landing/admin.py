from django.contrib import admin
from .models import UserLead
# Register your models here.


class UserLeadAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'dateEntered']
    class Meta:
        model = UserLead


admin.site.register(UserLead, UserLeadAdmin)