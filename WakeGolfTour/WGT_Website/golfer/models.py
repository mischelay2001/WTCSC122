# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from operator import itemgetter

from django.db import models
from tournament.models import Tournament, Round


# from WGT_Website.tournament.models import Tournament, Round
# from golf_course.models import GolfCourse
# from WGT_Website.golf_course.models import GolfCourse

class Golfer(models.Model):
    golfer_id = models.IntegerField(primary_key=True)
    golfer_name = models.TextField()
    golfer_birthdate = models.DateField()
    golfer_city = models.TextField (default="unknown", blank=True)

    class Meta:
        managed = True
        db_table = 'Golfer'

    def __str__(self):
        return self.golfer_name


class TournGolfer(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    tg_tourn = models.ForeignKey(Tournament, models.DO_NOTHING)
    tg_golfer = models.ForeignKey(Golfer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TournGolfer'
        verbose_name = "Tournament Golfer"
        verbose_name_plural = "Tournament Golfers"

    def getGolferName(self):
        return self.tg_golfer.golfer_name

    def getTournName(self):
        return self.tg_tourn.tourn_name

    def getGolferID(self):
        return self.tg_golfer.golfer_id

    def __str__(self):
        return "{} {}".format(self.tg_tourn.tourn_name,
                              self.tg_golfer.golfer_name)


class GolferRoundScores(models.Model):
    grs_id = models.IntegerField(primary_key=True)
    grs_tourn_golfer = models.ForeignKey(TournGolfer, models.DO_NOTHING)
    grs_round = models.ForeignKey(Round, models.DO_NOTHING)
    grs_total_score = models.IntegerField()
    grs_hole1_score = models.IntegerField()
    grs_hole2_score = models.IntegerField()
    grs_hole3_score = models.IntegerField()
    grs_hole4_score = models.IntegerField()
    grs_hole5_score = models.IntegerField()
    grs_hole6_score = models.IntegerField()
    grs_hole7_score = models.IntegerField()
    grs_hole8_score = models.IntegerField()
    grs_hole9_score = models.IntegerField()
    grs_hole10_score = models.IntegerField()
    grs_hole11_score = models.IntegerField()
    grs_hole12_score = models.IntegerField()
    grs_hole13_score = models.IntegerField()
    grs_hole14_score = models.IntegerField()
    grs_hole15_score = models.IntegerField()
    grs_hole16_score = models.IntegerField()
    grs_hole17_score = models.IntegerField()
    grs_hole18_score = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'GolferRoundScores'
        verbose_name = "Golfer Round Scores"
        verbose_name_plural = "Golfers Round Scores"

    def getTournScores(tourn_id):
        # the list to return
        tournament_scores = list()

        # get the list of tourn golfers for this tournament
        # using the filter method of TournGolfer.objects
        # with the tg_tourn equal to the passed in tourn_id
        tourn_golfers = TournGolfer.objects.filter(tg_tourn=tourn_id)

        # loop through the tourngolfer objects,
        # get the golfer name, tournament name
        # (use the helper functions) and the scores for
        # that golfer for each round of the tournament,
        for tourn_golfer in tourn_golfers:

            # clear total score and create new dictionary
            # object
            total_score = 0
            gts = dict()

            # get the golfer name and tournament name
            # using the tourn_golfer key and the helper
            # methods created above
            gts["golfer_name"] = tourn_golfer.getGolferName()
            gts["tournament_name"] = tourn_golfer.getTournName()

            # store the tourn_golfer_id for indexing later
            gts["tourn_golfer_id"] = tourn_golfer.tg_id

            # get the scores for this tourn_golfer from
            # the GolferRoundScores
            scores = GolferRoundScores.objects.filter(grs_tourn_golfer=tourn_golfer).order_by('grs_round')

            # loop through the scores for each round,
            # putting the score in the dict and adding
            # it to the total score for the tournament
            for i in range(1, len(scores) + 1):
                round_score = scores[i - 1].grs_total_score
                gts["round{}_score".format(i)] = round_score
                total_score = total_score + round_score
            # store the total score
            gts["total_score"] = total_score
            # add the dictionary entry to the list
            tournament_scores.append(gts)

        # return the list sorted by "total_score"
        return sorted(tournament_scores, key=itemgetter('total_score'))

    def getTournScoresByGolfer(golfer_id):
        # the list to return
        tournament_scores = list()

        # get the list of tourn golfers for this tournament
        # using the filter method of TournGolfer.objects
        # with the tg_tourn equal to the passed in golfer_id

        tourn_golfers = TournGolfer.objects.filter(tg_golfer=golfer_id)

        # loop through the tourngolfer objects,
        # get the golfer name, tournament name
        # (use the helper functions) and the scores for
        # that golfer for each round of the tournament,
        for tourn_golfer in tourn_golfers:

            # clear total score and create new dictionary
            # object
            total_score = 0
            gts = dict()

            gts["golfer_id"] = tourn_golfer.getGolferID()

            # get the golfer name and tournament name
            # using the tourn_golfer key and the helper
            # methods created above
            gts["golfer_name"] = tourn_golfer.getGolferName()
            gts["tournament_name"] = tourn_golfer.getTournName()

            # store the tourn_golfer_id for indexing later
            gts["tourn_golfer_id"] = tourn_golfer.tg_id

            # get the scores for this tourn_golfer from
            # the GolferRoundScores
            scores = GolferRoundScores.objects.filter(grs_tourn_golfer=tourn_golfer).order_by('grs_round')
            print(scores, "line 170")
            # loop through the scores for each round,
            # putting the score in the dict and adding
            # it to the total score for the tournament
            for i in range(1, len(scores) + 1):
                round_score = scores[i - 1].grs_total_score
                gts["round{}_score".format(i)] = round_score
                total_score = total_score + round_score
            # store the total score
            gts["total_score"] = total_score
            # add the dictionary entry to the list
            tournament_scores.append(gts)

        # return the list sorted by "tournament_name"
        return sorted(tournament_scores, key=itemgetter('tournament_name'))

    def getParDiffs(self):
        # 1. Add the import for the module containing the getattr function - from operator import itemgetter
        # (See import statements above)
        # variable for loop iteration
        i = 0
        # variable for number of rounds
        num_rounds = 18
        # 2. Create an empty score list to hold the golfer scores for the round.
        golf_scores_list = list()
        # 3. Using a for loop with the range function to loop 18 times, append each of the scores retrieved using the
        # getattr function shown above to the score list created in step 2.
        for a in range(num_rounds):
            score = getattr(self, 'grs_hole{}_score'.format(i + 1))
            golf_scores_list.append(score)
            i += 1
        # 4. Retrieve the par list by calling getParList
        # Not part of loop from step 3
        parList = self.grs_tourn_golfer.tg_tourn.tourn_course.getParList()
        # 5. Create an empty round_scores_diff list to hold the 18 2-element lists that contains the score and par
        # difference for each hole played for a round.
        round_scores_diff_list = list()
        # 6. Using another for loop with the range function to loop 18 times, do the following:
        for b in range(num_rounds):
            # a. Create an empty hole_score_par_diff list to hold the 2-element list that contains the score and par
            # difference for this hole.
            hole_score_par_diff_list = list()
            # b. get the score for this hole from the score list
            hole_score = golf_scores_list[b]
            # c. get the par for this hole from the par list
            hole_par = parList[b]
            # d. Get the par difference by subtracting the par from the score
            par_diff = hole_score - hole_par
            # e. Append the score the to the hole_score_par_diff list.
            hole_score_par_diff_list.append(hole_score)
            # f. Append the par difference to the hole_score_par_diff list.
            hole_score_par_diff_list.append(par_diff)
            # g. Append the hole_score_par_diff list to the round_scores_diff list.
            round_scores_diff_list.append(hole_score_par_diff_list)
        # 7. Return the round_scores_diff list.
        return round_scores_diff_list

    def __str__(self):
        return "{} {} {} {}".format(self.grs_tourn_golfer.tg_golfer,
                                    self.grs_tourn_golfer.tg_tourn,
                                    self.grs_round, self.grs_total_score)
