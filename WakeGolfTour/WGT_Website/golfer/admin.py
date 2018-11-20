# Register your models here.
from django.contrib import admin

from .models import Golfer, TournGolfer, GolferRoundScores


class GolferAdmin(admin.ModelAdmin):
    list_display = ['golfer_name', 'golfer_birthdate']
    list_filter = ['golfer_name']
    exclude = ['golfer_id']
    actions_on_top = False


class TournGolferAdmin(admin.ModelAdmin):
    list_display = ['tg_golfer', 'tg_tourn']
    list_filter = ['tg_tourn']
    search_fields = ['tg_golfer__golfer_name']
    exclude = ['tg_id']
    actions_on_top = False


class GolferRoundScoresAdmin(admin.ModelAdmin):
    list_display = ['golferName', 'tournName', 'grs_round', 'grs_total_score']
    list_filter = ['grs_tourn_golfer__tg_tourn']
    ordering = ['grs_round']
    search_fields = ['grs_tourn_golfer__tg_golfer__golfer_name']
    exclude = ['grs_id']
    actions_on_top = False

    fieldsets = [(None, {'fields': ['grs_tourn_golfer']}),
                 (None, {'fields': [('grs_total_score', 'grs_round')]}),
                 ('Scores (Front Nine)', {'fields': [
                     ('grs_hole1_score', 'grs_hole2_score', 'grs_hole3_score'),
                     ('grs_hole4_score', 'grs_hole5_score', 'grs_hole6_score'),
                     ('grs_hole7_score', 'grs_hole8_score', 'grs_hole9_score')
                 ]}),
                 ('Scores (Back Nine)', {'fields': [
                     ('grs_hole10_score', 'grs_hole11_score', 'grs_hole12_score'),
                     ('grs_hole13_score', 'grs_hole14_score', 'grs_hole15_score'),
                     ('grs_hole16_score', 'grs_hole17_score', 'grs_hole18_score')
                 ]})]

    # This method returns the tournament name from the
    # TournGolfer class object, using the ForeignKey link
    def tournName(self, grs):
        return grs.grs_tourn_golfer.tg_tourn.tourn_name
        # Use this next statement for changing the column name.

    tournName.short_description = 'Tournament'

    # This method returns the golfer name from the
    # TournGolfer class object, using the ForeignKey link
    def golferName(self, grs):
        return grs.grs_tourn_golfer.tg_golfer.golfer_name

    # Use this next statement for changing the column name.
    golferName.short_description = 'Golfer'

    # This method removes the Delete Button from the Admin pages.
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Golfer, GolferAdmin)
admin.site.register(TournGolfer, TournGolferAdmin)
admin.site.register(GolferRoundScores, GolferRoundScoresAdmin)
