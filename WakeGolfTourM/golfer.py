# Import Statements
from valid_entry import clean_birthdate_yyyymmdd

class Golfer:
    """Golfer object derived from data in the golfersInput.csv

    Attributes:
        golfer_id          a unique id for this golfer (to be used as a primary key when stored in the database)
        golfer_name        the name for the golfer
        golfer_birthdate   the golfers birthdate
                           NOTE: golfersInput.csv has this field in the format 'mm-dd-yy',
                                 but the database expects it in the format 'YYYY-mm-dd', so it needs converted

    """

    def __init__(self, a_id_golfer, a_name_golfer, a_birthdate_golfer, a_address_golfer):
        """
        constructor of class Golfer
        """
        self.__golfer_id = a_id_golfer
        self.__golfer_name = a_name_golfer
        self.__golfer_birthdate = self.to_SQL_date(a_birthdate_golfer)
        self.__golfer_address = a_address_golfer

    ### Please complete the following functions
    
    def get_golfer_id(self):
        """
        return the golfer_id to the caller
        """
        return self.__golfer_id

    def get_golfer_name(self):
        """
        return the golfer_name to the caller
        """
        return self.__golfer_name
    
    def get_golfer_birthdate(self):
        """
        return the golfer_birthdate to the caller
        """
        return self.__golfer_birthdate

    def to_SQL_date(self,a_birthdate_golfer):
        """
        convert csv date ('mm-dd-yy') to sql date ('YYYY-mm-dd')
        """
        entry = a_birthdate_golfer
        clean_birthdate_yyyymmdd(entry)
        return entry

    def get_golfer_address(self):
        """
        return the golfer_address to the caller
        """
        return self.__golfer_address

    def __str__(self):
    #     """
    #     return a comma-delimiter string
    #     of the instance variable values
    #     """
        cvs_string = str(str(self.__golfer_id) +  "," + str(self.__golfer_name)
                         + "," + str(self.__golfer_birthdate) + "," + str(self.__golfer_address))

        return cvs_string
