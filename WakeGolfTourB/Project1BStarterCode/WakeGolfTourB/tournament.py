class Tournament:
    """
    Tournament object derived from data in the tournamentsInput.csv

    Instance variables:
        tourn_id       a unique id for this tournament (to be used as a primary key when stored in the database)
        tourn_name     the name for the tournament
        course_id      the id of the golf course where the tournament was played
        start_date     the date of the first round of this tournament
                       NOTE: tournamentsInput.csv has this field in the format 'm-dd-yy',
                             but the database expects it in the format 'YYYY-mm-dd',
                             so it needs converted

        num_rounds     number of rounds for this tournament (2, 3, or 4)
        num_golfer     number of golfers that played in the tournament

    """

    def __init__(self, tourn_id, name, course_id, start_date,
                 num_rounds, num_golfers):
        """
        constructor of class Tournament
        """
        self.__tourn_id = tourn_id
        self.__tourn_name = name
        self.__course_id = course_id
        self.__start_date = self.to_SQL_date(start_date)
        self.__num_rounds = num_rounds
        self.__num_golfers = num_golfers

    ### Please complete the following functions
        
    # get_tourn_id
        """
        return the tourn_id to the caller
        """

    # get_tourn_name
        """
        return the tourn_name to the caller
        """

    # get_course_id
        """
        return the course_id to the caller
        """

    # get_start_date
        """
        return the start_date to the caller
        """

    # get_num_rounds
        """
        return the num_rounds to the caller
        """

    # get_num_golfers
        """
        return the num_golfers to the caller
        """

    # to_SQL_date(self, start_date):
        """
        convert csv date ('mm-dd-yy') to sql date ('YYYY-mm-dd')
        return the converted date
        """

    #  __str__
        """
        return a comma-delimiter string
        of the instance variable values
        """
