class Hole:
    """
    Hole object derived from data in the golfCoursesInput.csv

    Attributes:
        hole_id         a unique id for this hole (to be used as a primary key when stored in the database)
        course_id       the id of the golf course where this hole is played
        hole_num        the number of the hole (1-18)
        par             the par value for this hole (3,4, or 5)
    """

    ### Please complete the following functions

    def __init__(self, a_id_hole, a_id_course, a_number_hole, a_number_par):
        """
        constructor of class Hole
        """
        self.__hole_id = a_id_hole
        self.__course_id = a_id_course
        self.__hole_num = a_number_hole
        self.__par = a_number_par

    def get_hole_id(self):

        """
        return the hole_id to the caller
        """

        return self.__hole_id

    def get_course_id(self):
        """
        return the course_id to the caller
        """

        return self.__course_id

    def get_hole_num(self):
        """
        return the hole_num to the caller
        """

        return self.__hole_num

    def get_par(self):
        """
        return the hole par to the caller
        """

        return self.__par

    def __str__(self):
        """
        create a comma-delimiter string
        of the instance variable values
        """

        cvs_string = str(str(self.__hole_id) +  "," + str(self.__course_id) +  "," + str(self.__hole_num) +  ","
                         + str(self.__par))

        return cvs_string
