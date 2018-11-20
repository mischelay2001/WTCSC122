class JSONGolferRoundScores(object):
    # Add needed code - note initialize all hole scores to 0

    def __init__(self, tournGolferId, roundId):
        self.model = "golfer.golferroundscores"
        self.fields = {"grs_tourn_golfer": tournGolferId,
                       "grs_round": roundId,
                       "grs_total_score": 0,
                       "grs_hole1_score": 0,
                       "grs_hole2_score": 0,
                       "grs_hole3_score": 0,
                       "grs_hole4_score": 0,
                       "grs_hole5_score": 0,
                       "grs_hole6_score": 0,
                       "grs_hole7_score": 0,
                       "grs_hole8_score": 0,
                       "grs_hole9_score": 0,
                       "grs_hole10_score": 0,
                       "grs_hole11_score": 0,
                       "grs_hole12_score": 0,
                       "grs_hole13_score": 0,
                       "grs_hole14_score": 0,
                       "grs_hole15_score": 0,
                       "grs_hole16_score": 0,
                       "grs_hole17_score": 0,
                       "grs_hole18_score": 0}


def main():
    standaloneDjango()
    jsonStr = getJSONstr()
    writeJSONstr(jsonStr)


def standaloneDjango():
    import os
    import django
    import json

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wgt_site.settings")
    django.setup()


def getTournID():
    from django.db import models
    from tournament.models import Tournament

    newTournObj = Tournament.objects.get(
        tourn_name="Oak City Championship")
    return newTournObj.tourn_id


def getGolferID(name_to_get):
    from django.db import models
    from golfer.models import Golfer
    newGolfer = Golfer.objects.get(golfer_name=name_to_get)
    print(newGolfer, "new golfer", newGolfer.golfer_id)
    return newGolfer.golfer_id


def getTournGolferID(golfer_id, tourn_id):
    from django.db import models
    from golfer.models import TournGolfer

    tourn_golfer_id = 0

    tourn_golfers = TournGolfer.objects.filter(tg_tourn=tourn_id)

    for tourn_golfer in tourn_golfers:
        print(tourn_golfer.tg_golfer.golfer_id, "line 69", golfer_id)
        if tourn_golfer.tg_golfer.golfer_id == golfer_id:
            tourn_golfer_id = tourn_golfer.tg_id
            print(tourn_golfer_id, "line 72")
            break

    return tourn_golfer_id


def getRoundIDs(tourn_id):
    from django.db import models
    from tournament.models import Round

    round1_id = 0
    round2_id = 0

    rounds = Round.objects.filter(round_tourn_id=tourn_id)

    for tourn_round in rounds:
        if tourn_round.round_day == "Sat":
            round1_id = tourn_round.round_id
        else:
            round2_id = tourn_round.round_id

    return round1_id, round2_id


def readScores():
    import csv
    input_file = open('golferScores.csv', 'r')
    input_file = csv.reader(input_file)
    return input_file


def getJSONstr():
    # Add needed code
    import json
    scores = []
    scores = readScores()
    tourn_id = getTournID()
    round1_id, round2_id = getRoundIDs(tourn_id)

    round_scores = []

    for score in scores:
        golfer_id = getGolferID(score[0].strip())

        tourn_golfer_id = getTournGolferID(golfer_id, tourn_id)

        if score[2] == 'Sat':
            grs = JSONGolferRoundScores(tourn_golfer_id, round1_id)
        else:
            grs = JSONGolferRoundScores(tourn_golfer_id, round2_id)

        scores_list = list(map(int, score[3:]))

        round_score = 0  # ;
        j = 1
        for sc in scores_list:
            grs.fields["grs_hole{}_score".format(j)] = sc
            round_score = round_score + sc
            j = j + 1

        grs.fields["grs_total_score"] = round_score

        json_grs = json.dumps(grs.__dict__)
        round_scores.append(json_grs)

    jsonStr = str(round_scores).replace("'", '')

    return jsonStr


def writeJSONstr(jsonStr):
    outFile = open('golfer_round_scores_data.json', 'w')
    outFile.write(jsonStr)
    outFile.close()


main()
