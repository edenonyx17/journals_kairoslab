from django.contrib import admin
from .models import journal

# Register your models here.
@admin.register(journal)
class journalAdmin(admin.ModelAdmin):
    list_display = ('topic', 'body', 'writer', 'date_created', 'date_updated')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.writer = request.user
        super().save_model(request, obj, form, change)