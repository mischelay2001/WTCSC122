# Import Statements
from valid_entry import clean_date_yyyymmdd

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

    def __init__(self, a_id_tournament, a_name_tournament, a_id_golf_course, a_date_start,
                 a_number_round, a_number_golfers):
        """
        constructor of class Tournament
        """
        self.__tourn_id = a_id_tournament
        self.__tourn_name = a_name_tournament
        self.__course_id = a_id_golf_course
        self.__start_date = self.to_SQL_date(a_date_start)
        self.__num_rounds = a_number_round
        self.__num_golfers = a_number_golfers

    ### Please complete the following functions

    def get_tourn_id(self):
        """
        return the tourn_id to the caller
        """
        return self.__tourn_id

    def get_tourn_name(self):
        """
        return the tourn_name to the caller
        """
        return self.__tourn_name

    def get_course_id(self):
        """
        return the course_id to the caller
        """
        return self.__course_id

    def get_start_date(self):
        """
        return the start_date to the caller
        """
        return self.__start_date

    def get_num_rounds(self):
        """
        return the num_rounds to the caller
        """
        return self.__num_rounds

    def get_num_golfers(self):
        """
        return the num_golfers to the caller
        """
        return self.__num_golfers

    def to_SQL_date(self, a_date_start):
        """
        convert csv date ('mm-dd-yy') to sql date ('YYYY-mm-dd')
        return the converted date
        """
        entry = clean_date_yyyymmdd(a_date_start)

        return entry

    def __str__(self):
        """
        return a comma-delimiter string
        of the instance variable values
        """
        csv_string = str(str(self.__tourn_id) +  "," + str(self.__tourn_name) +  "," + str(self.__course_id) +  ","
                         + str(self.__start_date) + "," + str(self.__num_rounds) + "," + str(self.__num_golfers))

        return csv_string
