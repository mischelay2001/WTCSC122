# Register your models here.
from django.contrib import admin

# from .models import Tournament, Round
from .models import Tournament


class TournamentAdmin(admin.ModelAdmin):
    list_display = ['tourn_name', 'tourn_course', 'tourn_start_date']
    list_filter = ['tourn_course']
    ordering = ['tourn_start_date']
    exclude = ['tourn_id']
    actions_on_top = False

    # This method removes the Delete Button from the Admin pages.
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Tournament, TournamentAdmin)
