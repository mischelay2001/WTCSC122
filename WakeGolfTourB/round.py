class Round:
    """
    Round object derived from data in the tournamentInput.csv

    Instance variables:
        round_id        a unique id for this round (to be used as a primary key when stored in the database)
        tourn_id        the id of the tournament for this round
        day             the day that the round was played ('Thu', 'Fri', 'Sat', 'Sun')
    """
    ### Please complete this class  

    def __init__(self, a_id_round, a_id_tournament, a_name_day):
        """
        constructor of class Tournament
        """
        self.__round_id = a_id_round
        self.__tourn_id = a_id_tournament

        self.__day_of_week = a_name_day


    ### Please complete the following functions

    def get_round_id(self):
        """
        return the round_id to the caller
        """
        return self.__round_id

    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    def get_day_of_week(self):
        """
        return the day_of_week to the caller
        """
        return self.__day_of_week

    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_string = str(str(self.__round_id) +  "," + str(self.__tourn_id) +  "," + str(self.__day_of_week))

        return csv_string
