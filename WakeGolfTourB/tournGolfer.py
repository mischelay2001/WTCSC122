class TournGolfer:
    """
    TournGolfer object derived from data in the tournamentInput.csv

    Instance variables:
        tourn_golfer_id    a unique id for this tourn_golfer (to be used as a primary key when stored in the database)
        tourn_id           the id of the tournament played by the golfer
        golfer_id          the id of the golfer playing in the tournament

    """
    ### Please complete this class   
    
    def __init__(self, a_id_tourn_golfer, a_id_tourn, a_golfer_id):
        """
        constructor of class Tournament
        """
        self.__tourn_golfer_id = a_id_tourn_golfer
        self.__tourn_id = a_id_tourn
        self.__golfer_id = a_golfer_id

    ### Please complete the following functions

    def get_tourn_golfer_id(self):
        """
        return the tourn_golfer_id to the caller
        """
        return self.__tourn_golfer_id

    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    def get_golfer_id(self):
        """
        return the golfer_id to the caller
        """
        return self.__golfer_id

    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_string = str(str(self.__tourn_golfer_id) +  "," + str(self.__tourn_id) +  "," + str(self.__golfer_id))

        return csv_string
