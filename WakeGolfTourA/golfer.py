# Import Statements
from valid_entry import clean_date_yyyymmdd

class Golfer:
    """Golfer object derived from data in the golfersInput.csv

    Attributes:
        golfer_id          a unique id for this golfer (to be used as a primary key when stored in the database)
        golfer_name        the name for the golfer
        golfer_birthdate   the golfers birthdate
                           NOTE: golfersInput.csv has this field in the format 'mm-dd-yy',
                                 but the database expects it in the format 'YYYY-mm-dd', so it needs converted

    """

    def __init__(self, a_id_golfer, a_name_golfer, a_birthdate_golfer):
        """
        constructor of class Golfer
        """
        self.__golfer_id = a_id_golfer
        self.__golfer_name = a_name_golfer
        self.__golfer_birthdate = self.to_SQL_date(a_birthdate_golfer)

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
        # Initiate variable to string
        entry = a_birthdate_golfer

        # Clean unwanted spaces and characters
        entry = entry.strip()
        clean_chr = ["(", ")", "\\", ".", ",", " "]
        for i in clean_chr:
            entry = entry.replace(i, "")

        # Ensure only - is the delimited character
        date_chr = ["/", "-"]
        for i in date_chr:
            entry = entry.replace(i, "-")

        # Separate into month, day, year
        entry = entry.split("-")
        date_month = int(entry[0])
        date_day = int(entry[1])
        date_year = int(entry[2])

        # Find length of month, day, year
        len_month = len(str(date_month))
        len_day = len(str(date_day))
        len_year = len(str(date_year))

        # Ensure full two-digit month and day
        if len_month < 2 and date_month < 10:
            date_month = "0" + str(date_month)

        if len_day < 2 and date_day < 10:
            date_day = "0" + str(date_day)

        # Ensure full four-digit year and correct century
        if len_year < 4:
            if date_year == 0:
                date_year = "2000"
            elif 0 < date_year <= 9:
                date_year = "200" + str(date_year)
            elif 9 < date_year <= 12:
                date_year = "20" + str(date_year)
            elif 12 < date_year <= 99:
                date_year = "19" + str(date_year)

        # Convert date into yyyy/mm/dd format
        entry = (str(date_year) + "-" + str(date_month) + "-" + str(date_day))

        return entry

    def __str__(self):
    #     """
    #     return a comma-delimiter string
    #     of the instance variable values
    #     """
        cvs_string = str(str(self.__golfer_id) +  "," + str(self.__golfer_name)
                         + "," + str(self.__golfer_birthdate))

        return cvs_string
