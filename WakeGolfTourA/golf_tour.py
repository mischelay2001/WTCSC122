import csv

from golfCourse import GolfCourse
from hole import Hole
from golfer import Golfer


def main():
    """
    Algorithm:
    1.  Initialize the input and output file names
    2.  Initialize the database and table names for output
    3.  Call create_golf_courses function, passing in the the input
        file name, and retrieving the returned golf_course_list,
        a list of GolfCourse objects containing information for 5 
        golf courses and the returned golf_course_holes_dict which 
        has the golf_course_id as the key, and the value is a list 
        of 18 tuples containing (hole_num, par_value).
    4.  Call create_holes function, passing in the 
        golf_course_holes_dict and retrieving the returned 
        holes_list, a list of Hole objects containing information 
        for 90 (5*18) golf course holes
    5.  Call create_golfers function, passing in the input file name, 
        and retrieving the returned golfer_list, a list of Golfer 
        objects containing information for 30 golfers
    6.  Write out the class objects to files from:
        create_golf_courses, create_holes, create_golfers
     """
    print("Wake Golf Tour Project 1")

    # 1. Initialize the input and output file names

    golf_courses_infile = "golfCoursesInput.csv"
    golfers_infile = "golfersInput.csv"
    tournaments_infile = "tournamentsInput.csv"
    golfer_scores_infile = "roundScoresInput.csv"

    golf_courses_file = "golfCourses.csv"
    holes_file = "holes.csv"
    golfers_file = "golfers.csv"
    tournaments_file = "tournaments.csv"
    tourn_golfers_file = "tournGolfers.csv"
    rounds_file = "rounds.csv"
    golfer_scores_file = "golferRoundScores.csv"

    # 2. Initialize the database and table names for output

    database_name = "WakeGolfTour.db"
    golf_courses_table = "GolfCourse"
    holes_table = "Hole"
    golfers_table = "Golfer"
    tournaments_table = "Tournament"
    tourn_golfers_table = "TournGolfer"
    rounds_table = "Round"
    golfer_scores_table = "GolferRoundScores"

    # 3. Call create_golf_courses function, passing in the input
    #    file name, and retrieving the returned golf_courses_list,
    #    a list of 5 golf course objects and the golf_course_holes_dict,
    #    containing information about the holes for each of the golf courses

    golf_course_list, golf_course_holes_dict = create_golf_courses(golf_courses_infile)

    # 4. Call create_holes function, passing in the golf_course_holes_dict
    #    and retrieving the returned holes_list, a list of Hole objects 
    #    containing information for 90 golf course holes

    holes_list = create_holes(golf_course_holes_dict)

    # 5. Call create_golfers function, passing in the input
    #    file name, and retrieving the returned golfer_list, 
    #    a list of 30 golfer objects

    golfer_list = create_golfers(golfers_infile)

    # 6. Write out the lists returned from the create functions:
    #    create_golf_courses, create_golfers, create_tournaments

    write_objs_to_file(golf_courses_file, golf_course_list)
    write_objs_to_file(holes_file, holes_list)
    write_objs_to_file(golfers_file, golfer_list)


def create_golf_courses(filename):
    """
    Each line of input contains:
    golf_course_name, par_h1, par_h2, ..., par_h18

    where golf_course_name is the name of the golf course and each
          par_h# is a par value for the hole #.
    
    Note: string input needs to be stripped of any whitespace
          integer strings need to be changed to ints 

    Algorithm:
    1. Create an empty list called golf_course_list that will contain
       GolfCourse objects whose data comes from the input file
    2. Create a dictionary, golf_course_holes_dict, having the golf_course_id as the key,
       and a list of 18 tuples containing (hole_num, par_value) as the value
       Each entry will have:
         golf_course_id: [(hole_num, par_value), 
                          (hole_num, par_value), ..., 
                          (hole_num, par_value)]
    3. Initialize the golf_course_id to 1
    4. Use a try/except block to capture a File Not Found Error
        a. Open the input file object for reading the input file
        b. Call the csv.reader function, passing in the input file
           and capturing the CSV file contents.
        c. Create a list from the file contents: courses_list
        d. Create an outer loop to read each golf course in courses_list
           Outer Loop
            1. Get the golf course name from the first element stripped of whitespace.
            2. Create an empty list, hole_info,  to hold the hole information
            3. Create an inner loop to traverse the 18 hole
               par values using the range function
               Inner Loop
                 a. Convert the string hole par values to ints
                 b. Add par value to total par
                 c. Append hole_num and par value to the hole_info list

            3. Add entry for this golf course's hole_info to the golf_course_holes_dict
            4. Create a new GolfCourse object, call it golf_course,
               passing in golf_course_id, golf_course_name, and total_par
            5. Append the golf_course object to the golf_course_list
            6. Increment the golf_course_id

        e. Close input_file object
    3. Print each golf_course object in the golf_course_list to the console
    4. Return the golf_course_list
    """

    print("\nGolf Course List: golf_course_list\n")

    # Algorithm:
    # 1. Create an empty list called golf_course_list that will contain
    #    GolfCourse objects whose data comes from the input file

    golf_course_list = []

    # 2. Create an empty dictionary called golf_course_holes_dict
    #    whose key is the golf_course_id and the value is a tuple
    #    containing hole_number and par_value

    golf_course_holes_dict = dict()

    # 3. Initialize the golf_course_id to 1

    golf_course_id = 1

    # 4. Use a try/except block to capture a File Not Found Error

    try:
        # a. Open the input_file object for reading the input file

        input_file = open(filename, 'r')

        # b. Call the csv.reader function, passing in the input file
        #    and capturing the CSV file contents.

        file_lines = csv.reader(input_file)

        # c. Create a list from the file contents: courses_list

        courses_list = list(file_lines)

        # d. Create an outer loop to read each golf course in
        #    courses_list

        for golf_course in courses_list:

            # Outer Loop
            # 1. The first element (golf course name) is stripped
            #    of whitespace.

            golf_course_name = golf_course[0].strip()

            # 2. Create an inner loop to traverse the 18 hole
            #    par values using the range function

            total_par = 0
            holes = []
            for i in range(1, 19):
                # Inner Loop
                # a. Convert the string hole par values to ints
                par = int(golf_course[i])

                # b. Add value to total par
                total_par = total_par + par

                # c. Append hole_num and par to list for dictionary
                holes.append((i, par))

            # 2. Add entry for this golf course's holes to the golf_course_holes_dict
            golf_course_holes_dict[golf_course_id] = holes

            # 4. Create a new GolfCourse object, call it golf_course,
            #    passing in golf_course_id, golf_course_name, and total_par

            golf_course = GolfCourse(golf_course_id, golf_course_name, total_par)

            # 5. Append the golf_course object to the golf_course_list

            golf_course_list.append(golf_course)

            # 6. Increment the golf_course_id

            golf_course_id = golf_course_id + 1

        # e. Close input_file object

        input_file.close()

    except IOError:
        print("File Not Found Error.")

    # 4. Print the golf_course_list objects to the console

    for gc in golf_course_list:
        print(gc)

    # 5. Return the golf_course_list and golf_course_holes_dict

    return golf_course_list, golf_course_holes_dict


def create_holes(golf_course_holes_dict):
    """
    Use the dictionary created in the create_golf_courses function
    to create a list of Hole objects. It has the golf_course_id as the key,
    and a list of 18 tuples containing (hole_num, par_value) as the value
        Each entry will have:
         golf_course_id: [(hole_num, par_value), 
                          (hole_num, par_value), ..., 
                          (hole_num, par_value)]

    Algorithm:
    1.  Create an empty list called holes_list that will contain
        Hole objects whose data comes from the input file
    2.  Initialize the hole_id to 1
    3.  Create an outer loop to read the golf course dictionary using the items() method
        retrieving the key (golf_course_info), and hole information (hole_info)
        Outer Loop:
        for golf_course_id, hole_info in golf_course_holes_dict.items():
          
            Create an inner loop to read each golf course's hole information (hole_info)
            Inner Loop
            for info in hole_info:
                a. Create a new Hole object, call it hole_obj, passing in
                   hole_id, golf_course_id, hole_num, and par_value
                b. Append the hole object to the holes_list
                c. Increment hole_id
    4. Print the holes_list objects to the console
    5. Return the holes_list
    """
    print("\nThe Hole object list: holes_list\n")

    ### create_holes function; author: Michele Johnson

    # empty list object; will hold hole ID, course ID, hole number, par value
    holes_list = []
    # initialize hole ID as integer and 0
    hole_id = 0
    # loop through course ID in golf_course_holes_dict; course_ID = dictionary key
    for key_course_id, hole_data in golf_course_holes_dict.items():
        # determine the number of value data sets per key
        hole_data_count = len(hole_data)
        # loop through each value data sets to capture elements separately
        for i in range(hole_data_count):
            hole_data_item = hole_data[i]
            # for current data set, capture hole number
            hole_number = hole_data_item[0]
            # for current data set, capture par value
            par_value = hole_data_item[1]
            # for current data set, increment hole ID
            hole_id += 1
            # initiate class: Hole
            a_hole = Hole(hole_id, key_course_id, hole_number, par_value)
            # append elements into holes_list
            holes_list.append(a_hole)
    # loop through holes_list and print
    for g in holes_list:
        print(g)

    return holes_list


def create_golfers(filename):
    """
    Each line of input contains:
    golfer_name, golfer_birthdate

    where golfer_name is the name of the golfer and
          golfer_birthdate is the day the golfer was born.

    Note: string input needs to be stripped of any whitespace

    Create a Golfer object from each line in the input file:
    containing -
    golfer_id, golfer_name, golfer_birthdate

    A list is returned, where each element is a Golfer object

    Algorithm:
    1. Create an empty list called golfer_list that will be
       filled in with Golfer objects whose data comes from
       the input file
    2. Initialize the golfer_id to 1
    3. Use a try/except block to capture a File Not Found Error
        a. Open the input file object for reading the input file
        b. Call the csv.reader function, passing in the input file
           and capturing the CSV file contents.
        c. Create a list from the file contents: golfer_input_list
    
        d. Create a loop to traverse the golfer_input_list,
           where the loop variable 'golfer_info' will contain one of
           the inner lists in golfer_list at each loop iteration
        Loop:
           1. Get the golfer_name and golfer_birthdate
           2. Create a new Golfer object, call it player, passing
              in golfer_id, golfer_name, and golfer_birthdate
           3. Append the player object to the golfer_list
           4. Increment the golfer_id
        e. close the input file
    4. Print the golfer_list objects to the console
    5. Return the golfer_list

    """

    print("\nThe Golfer object list:  golfer_list\n")

    ### create_golfer function; author: Michele Johnson """

    # empty list object; will hold golfer ID, golfer_name, golfer_birthdate
    golfer_list = []
    # initialize golfer ID as integer and 0
    golfer_id = 0
    # import input file
    import csv
    with open(filename, newline='') as csvfile:
        a_file = csv.reader(csvfile, delimiter=',', quotechar='|')
        # loop through each row of input
        for row in a_file:
            # for current row, increment golfer ID
            golfer_id += 1
            # for current row, capture and strip golfer name
            golfer_name = row[0].strip()
            # for current row, capture and strip golfer birthdate
            golfer_birthdate = row[1].strip()
            # initialize class: Golfer
            a_golfer = Golfer(golfer_id, golfer_name, golfer_birthdate)
            # append elements into golfer_list
            golfer_list.append(a_golfer)
    # loop through golfer_list and print
    for g in golfer_list:
        print(g)
    return golfer_list


def write_objs_to_file(filename, object_list):
    """
    This function takes a nested_list as input and writes it
    out to a csv file, where each line is a inner list

    Algorithm:
    1. Open the output file object for writing
    2. Create a loop to traverse the object_list parameter,
       where the loop variable is each object in the list:
       Loop:
       a. Set a str_obj string variable to the result of
          converting 'object' to a string using the
          __str__ method of the output file.  This can be
          accomplished by passing the object into the
          str() function.
       b. Add a new line character to the end of the
          str_obj string
       c. Use the write method of the output file object to
          write the str_obj string to the output file,
    3. Close the output file
    """
    # 1. Open the output file object for writing

    output_file = open(filename, 'w')

    # 2. Create a loop to traverse the object_list parameter,
    #    where the loop variable is each object in the list:

    for obj in object_list:
        # Loop:
        # a. Set a str_obj string variable to the result of
        #    converting 'object' to a string using the
        #    __str__ method of the output file.  This can be
        #    accomplished by passing the object into the
        #    str() function.

        str_obj = str(obj)

        # b. Add a new line character to the end of the
        #     str_obj string

        str_obj += '\n'

        # c. Use the write method of the output file object
        #    to write the str_obj string to the output file,

        output_file.write(str_obj)

    # 3. Close the output file

    output_file.close()


main()
