class GolfCourse:
    """
    GolfCourse object derived from data in the golfCoursesInput.csv

    Attributes:
        course_id      a unique id for this golf course (to be used as a primary key when stored in the database)
        course_name    the name for the golf course
        total_par      the total par for this course
    """

    
    def __init__(self, a_id_course, a_name_course, a_total_par):
        """
        constructor of class GolfCourse
        """
        self.__course_id = a_id_course
        self.__course_name = a_name_course
        self.__total_par = a_total_par

    def get_course_id(self):  # course_id
        """
        return the course_id to the caller
        """
        return self.__course_id

    def get_course_name(self):  # course_name
        """
        return the course_name to the caller
        """
        return self.__course_name

    def get_total_par(self):  # total_par
        """
        return the total_par to the caller
        """
        return self.__total_par

    def __str__(self):
        """
        create a comma-delimiter string
        of the instance variable values
        """
        csv_str = str(self.__course_id) + ',' + self.__course_name + \
                 ',' + str(self.__total_par)

        return csv_str
