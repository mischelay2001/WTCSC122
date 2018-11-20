class GolfCourse:
    """
    GolfCourse object derived from data in the golfCoursesInput.csv

    Instance variables:
        course_id      a unique id for this golf course (to be used as a primary key when stored in the database)
        course_name    the name for the golf course
        total_par      the total par for this course
    """

    def __init__(self, course_id, name, tot_par):
        """
        constructor of class GolfCourse
        """
        self.__course_id = course_id
        self.__course_name = name
        self.__total_par = tot_par

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
        csvStr = str(self.__course_id) + ',' + self.__course_name + \
                 ',' + str(self.__total_par)

        return csvStr
