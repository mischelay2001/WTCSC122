
class JSONGolferRoundScores (object):
    def __init__ (self, tournGolferId, roundId):     
        # Add needed code - note initialize all hole scores to 0

def main():

    # Add needed code
    
def standaloneDjango():

    # Add needed code
    
def getTournID():

    # Add needed code
    
def getGolferID(name_to_get):

    # Add needed code
    
def getTournGolferID (golfer_id, tourn_id):            

    # Add needed code
    
def getRoundIDs (tourn_id):            

    # Add needed code
    
    return round1_id, round2_id 
    
def readScores():
    
    # Add needed code
    # This is the same code as in your 
    # create_golfer_scores function from Project 1

    
def getJSONstr():

    # Add needed code
    
    for score in scores:
        golfer_id = getGolferID(score[0])
        tourn_golfer_id = getTournGolferID (golfer_id, tourn_id)
        
        if score[2] == 'Sat':
            grs = JSONGolferRoundScores (tourn_golfer_id, round1_id)
        else:
            grs = JSONGolferRoundScores (tourn_golfer_id, round2_id)
        
        scores_list = list(map(int, score[3:]))
        
        round_score = 0;          
        j = 1
        for sc in scores_list:
            grs.fields["grs_hole{}_score".format(j)] = sc
            round_score = round_score + sc
            j = j + 1
                                 
        grs.fields["grs_total_score"] = round_score
            
        json_grs = json.dumps (grs.__dict__)   
        round_scores.append (json_grs)
         
    jsonStr = str (round_scores).replace ("'",'')
    
    return jsonStr
            
def writeJSONstr (jsonStr):
    
    # Add needed code
    
main()   
   

