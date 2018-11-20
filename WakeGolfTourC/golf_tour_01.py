
import csv

from golfCourse import GolfCourse
from hole import Hole
from golfer import Golfer
from tournGolfer import TournGolfer
from tournament import Tournament
from round import Round


def main():
    """
    Algorithm:
    1.  Initialize the input and output file names
    2.  Initialize the database and table names for output
    3.  Call create_golf_courses function, passing in the the input
        file name, and retrieving the returned golf_course_list,
        a list of GolfCourse objects containing information for 5 golf courses
    4.  Call create_holes function, passing in the golf_course_holes_dict
        and retrieving the returned holes_list,
        a list of Hole objects containing information for 90 golf course holes
    5.  Call create_golfers function, passing in the input
        file name, and retrieving the returned golfer_list,
        a list of Golfer objects containing information for 30 golfers
    6.  Write out the class objects to files from:
        crate_golf_courses, create_holes, create_golfers
        ---------------------------------------------------------
    7.  Call create_tournaments function, passing in the input
        file name, and retrieving the returned tournament_list,
        a list of Tournament objects containing information for 15 tournaments
        and a tournament golfers dictionary, tournament_golfers_dict,
        whose key is the tourn_id and the value is the list of golfers
        playing in that tournament
    8.  Call create_rounds function, passing in the tournament_list from above,
        and retrieving the returned rounds_list,
        a list of Round objects containing information for 45 tournament rounds
    9.  Call create_tourn_golfers function, using the tournament_golfers_dict
        and the golfer_list from above, retrieving the returned tourn_golfers_list
        a list of TournGolfer objects containing information for 225 tournament golfers
    10. Write out the class objects to files from:
        create_tournaments, create_rounds, create_tourn_golfers
        ---------------------------------------------------------        
    11. Call create_golfer_scores function, passing in the round scores input
        file name, golfer_list returned from the create_golfers
        function, tournament_list returned from the create_tournaments
        function, and tourn_golfers_list returned from the
        create_tourn_golfers function, and retrieving the
        returned golfer_scores_list
    12. Write out the class objects to files from:
        create_golfer_scores
       
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
    #    and retrieving the returned holes_list,
    #    a list of Hole objects containing information for 90 golf course holes

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

    # 7. Call create_tournaments function, passing in the input
    #    file name and golf_course_list, retrieving the returned tournament_list,
    #    a list of 15 tournament objects, and a dictionary with the tourn_id as the key
    #    and a list of golfers for that tournament as the value

    tournament_list, tourn_golfers_dict = create_tournaments(tournaments_infile, golf_course_list)

    # 8. Call create_rounds function, passing in the input
    #    file name and the tournament_list, retrieving the returned rounds_list,
    #    a list of Round objects

    rounds_list = create_rounds(tournament_list)

    # 9. Call create_tourn_golfers function, using tourn_golfers_dict
    #    and the golfers_list, retrieving the returned tourn_golfers_list,
    #    a list of TournGolfer objects

    tourn_golfers_list = create_tourn_golfers(tourn_golfers_dict, golfer_list)

    # 10. Write out the lists returned from the create functions:
    #    create_holes, create_rounds, create_tourn_golfers

    write_objs_to_file(tournaments_file, tournament_list)
    write_objs_to_file(rounds_file, rounds_list)
    write_objs_to_file(tourn_golfers_file, tourn_golfers_list)
    
    # 11. Call create_golfer_scores function, passing in the
    #     golfer_scores_list returned from the read_golfer_scores
    #     function, golfers_list returned from the read_golfers
    #     function, tourns_list returned from the create_tournaments
    #     function, rounds_list returned from the create_rounds
    #     function, and the tourn_golfers_list returned from the
    #     create_tourn_golfers function, and retrieving the
    #     returned golfer_scores_list

    golfer_scores_list = create_golfer_scores(golfer_scores_infile,
                                              golfer_list,
                                              tournament_list,
                                              rounds_list,
                                              tourn_golfers_list)

    # 12. Write out the class objects to a file from:
    #     create_golfer_scores

    write_objs_to_file(golfer_scores_file, golfer_scores_list)

def create_golf_courses(filename):
    """
    Each line of input contains:
    golf_course_name, par_h1, par_h2, ..., par_h18

    where golf_course_name is the name of the golf course and each
          par_h# is a par value for the hole #.

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Algorithm:
    1. Create an empty list called golf_course_list that will contain
       GolfCourse objects whose data comes from the input file
    2. Create a dictionary, golf_course_holes_dict, it will have the golf_course_id as the key,
       and the value will be a list of 18 tuples containing (hole_num, par_value)
         golf_course_id: [(hole_num, par_value), (hole_num, par_value), ..., (hole_num, par_value)]
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
                 b. add par value to total par
                 c. append hole_num and par value to the hole_info list

            3. Add entry for this golf course's hole_info to the golf_course_holes_dict
            4. Create a new GolfCourse object, call it golf_course,
               passing in golf_course_id, golf_course_name, and total_par
            5. Append the golf_course object to the golf_course_list
            6. Increment the golf_course_id

        e. Close input_file object
    5. Print each golf_course object in the golf_course_list to the console
    6. Return the golf_course_list and golf_course_holes_dict
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

                # b. add value to total par
                total_par = total_par + par

                # c. append hole_num and par to list for dictionary
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

    # 5. Print the golf_course_list objects to the console

    for gc in golf_course_list:
        print(gc)

    # 6. Return the golf_course_list and golf_course_holes_dict

    return golf_course_list, golf_course_holes_dict


def create_holes(golf_course_holes_dict):
    """
    Use the dictionary built in the create_golf_courses function
    to create a list of Hole objects.
    The golf_course_holes_dict, has the golf_course_id as the key,
    and the value is a list of 18 tuples containing hole_num, par_value
        golf_course_id: [(hole_num, par_value), (hole_num, par_value), ..., (hole_num, par_value)]

    Algorithm:
    1.  Create an empty list called holes_list that will contain
        Hole objects whose data comes from the input file
    2.  Initialize the hole_id to 1
    3.  Create an outer loop to read the golf course dictionary
        retrieving the key (golf_course_info), and hole information (hole_info)
        Loop
          a.  Create an inner loop to read each golf course's hole information (hole_info)
              Loop
                1. Create a new Hole object, call it hole_obj, passing in
                   hole_id, golf_course_id, hole_num, and par_value
                2. Append the hole object to the holes_list
                3. Increment hole_id
          b. Close input_file object
    4. Print the holes_list objects to the console
    5. Return the holes_list
    """

    print("\nThe Hole object list:\n")

    ### Please provide your code here from Project 1-A 

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
    print ("\nThe Golfer object list:\n")

    ### Please provide your code here from Project 1-A 

    return golfer_list


def create_tournaments(filename, golf_course_list):
    """
    The tournamentsInput.csv has two different record types in the file.
    Hint: Open the file and see how it is organized.
    The first record type has

    golf_course_name, tournament_name, start_date, num_rounds, num_golfers

    where golf_course_name is the name of the golf course,
          tournament_name is the name of the tournament,
          start_date is the first day of the tournament,
          num_rounds is the number of rounds played in this tournament, and
          num_golfers is the number of golfers playing in this tournament

    The second record type is just a single golfer name.
    The number of these records is specified by the num_golfers field from the first record type
        golfer1_name
        golfer2_name
        ...
        golfer15_name

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Algorithm:
    1. Create a lookup map for golf_course_name to golf_course_id
       using the passed in golf_course_list
    2. Create an empty nested lists called tournament_list
       that will be filled in with data from the input file
    3. Initialize the tourn_id to 1 and the tourn_id_key to 0
    4. Use a try/except block to capture a File Not Found Error
        a. Open the input file object for reading the input file
        b. Call the csv.reader function, passing in the input file
           and capturing the CSV file contents.
        c. Create a list from the file contents: tournament_input_list
        d. Create a loop to traverse the tournament_input_list,
           where the loop variable 'tourn_info' will contain either the
           tournament information, or a golfer name
           Loop:
           1. Check the length of tourn_info, if it is one
              then this is golfer name, so add it to the tourn_golfers_dict.
              It will be used later in the create_tourn_golfers method.
              a. get the golfer name from tourn_info stripping whitespace
              b. add the golfer name to the tourn_golfers_dict
           2. If the length is greater than one, then process the tournament information
              a. Get each of the first five elements of the tourn inner list,
                 strip - course_name, tourn_name, start_date,
                 convert num_rounds and num_golfers to ints
              b. get golf_course id from lookup map
              c. Create a new Tournament object, call it tournament,
                 passing in tourn_id, tournament_name, golf_course_id,
                 start_date, num_rounds, and num_golfers
              d. Append the tournament object to the tourns_list
              e. Set the tourn_id_key = tourn_id
              f. Create dictionary entry for this key, the value is an empty list
                 to be filled in later
              g. Increment the tourn_id

        e. close the input file
    5. Print the tournament_list objects to the console
    6. Return the tournament_list and tourn_golfers_dict
    """
    print("\nThe Tournament object list:\n")
    
    ### Please provide your code here from Project 1-B 
    
    return tournament_list, tourn_golfers_dict

def create_rounds(tournament_list):
    """
    Use the tournament_list object list, that was
    returned from the create_tournaments function, which
    contains 15 Tournament objects with the following
    instance variables:

    tourn_id, tourn_name, golf_course_id, start_date,
    num_rounds, num_golfers, golfers...

    Create num_rounds Round objects from every
    Tournament object element in tourns_list:
    Add in the following as instance variables values

    round_id, tourn_id, day

    A list is returned, where each element is a Round object

    Algorithm:
    1. Create an empty list called rounds_list
       that will be filled in with Round objects
       whose data comes from the object list parameter
        - tournament_list
    2. Initialize the round_id
    3. Create an outer loop to to traverse the input
       tournament_list, where the loop variable 'tourn'
       will contain one of the Tournament objects in
       tournament_list at each loop iteration
       Outer Loop
       a. Get the number_rounds and tourn_id from the
          Tournament object, tourn, and initialize
          num_rounds to number_rounds - this will be
          decremented below to find the correct day
          for the Round object being built
       b. Create an inner loop to run number_round times
          using the range function, where the loop
          variable 'r' keeps the count for the
          number of Rounds being created
          Outer Loop
          1. Check the value of num_rounds to determne
             the day value of this Round object.
             Tournament oject, tourn
             Use a if/elif/else structure to set the
             day instance variable
             if num_rounds == 4: day = "Thu"
                num_rounds == 3: day = "Fri"
                num_rounds == 2: day = "Sat"
                num_rounds == 1: day = "Sun"
          2. Decrement the num_rounds counter
          3. Create a Round object call it round passing
             in round_id, tourn_id, and day
          4. Append the Round object to the rounds_list
          5. Increment the round_id
    4. Print the round objects to the console
    5. Return the rounds_list

    """
    print("\nThe Round object list\n")
    
    ### Please provide your code here from Project 1-B 

    return rounds_list


def create_tourn_golfers(tourn_golfers_dict,  golfer_list):
    """
    Use the tourn_golfers_dict, that was
    returned from the create_tournaments function, which contains
    entries with the key being the tourn_id, and the value is a list following format:
    of golfer_names

    Use the golfers_list object list parameter, that was
    returned from the create_golfers function, which
    contains 30 Golfer objects with the following instance
    variables:

    golfer_id, golfer_name, golfer_birthdate

    Create a TournGolfer object from every golfer_name listed
    in the tourn_golfers_dict.
    Add in the following as instance variables values -

        tourn_golfer_id, tourn_id, golfer_id

    A list is returned, where each element is a TournGolfer object

    Algorithm:
    1. Create a lookup map (golfer_name_to_id) for golfer_name to golfer_id
    2. Create an empty list called tourn_golfers_list
       that will be filled in with TournGolfer objects
       whose data comes from the nested list parameter,
       tournaments_list and object list parameter,
       golfers_list
    3. Initialize the tourn_golfer_id
    4. Create an outer loop to to traverse the input
       tourn_golfers_dict, where the key will contain the tournament id,
       and the value, 'golfer_name_list', will be the list of golfer names
       for that tournament
       Outer Loop
       a. Create an inner loop to traverse the
          golfer_name_list, where the loop variable
          'golfer_name' will contain one of the golfer names
          for the tournament
          Inner loop
          1. get golfer_id from (golfer_name_to_id) lookup map
          2. Create a TournGolfer object call it tourn_golfer,
             passing in tourn_golfer_id, tourn_id (from the dict key), and
             golfer_id
          3. Append the TournGolfer object to the
             tourn_golfers_list
          4. Increment the tourn_golfer_id

    4. Print the tourn_golfers_list objects to the console
    5. Return the tourn_golfers_list
    """

    print("\nThe TournGolfer object list\n")
    
    ### Please provide your code here from Project 1-B 

    return tourn_golfers_list

    
def create_golfer_scores(filename, golfer_list, tournament_list,
                         rounds_list, tourn_golfers_list):
    """
    Create GolferRoundScores objects from data in the input file,
    and using previously created object lists to convert names to ids.

    Each line of input contains:
        golfer_name, tourn_name, day, score_h1, score_h2, ..., score_h18

    where golfer_name is the name of the golfer,
          tourn_name is the name of the tournament,
          day is the round day,
          and each score_h# is the golfer's score for that hole

    Note: string input needs to be stripped of any whitespace
          int strings need to be changed to ints

    Use the golfers_list parameter, that was
    returned from the create_golfers function, with the
    following instance variables:

        golfer_id, golfer_name, golfer_birthdate

    Use the tourns_list parameter, that was
    returned from the create_tournaments function, with the
    following instance variables:

        tourn_id, tournament_name, golf_course_id, start_date,
        num_rounds, and num_golfers

    Use the rounds_list object list parameter, that was
    returned from the create_rounds function, with the
    following instance variables:

        round_id, tourn_id, day

    Use the tourn_golfers_list parameter, that was
    returned from the create_tourn_golfers function, with the
    following instance variables:

        tourn_golfers_id, tourn_id, golfer_id

    Create a GolferRoundScores object from every entry in the
    golfer_scores_list:  Add in the following as instance
    variables values:

        golfer_scores_id, tourn_golfer_id, round_id, total_round_score,
        and a list of scores (score_h1, score_h2, ..., score_h18)

    A list is returned, where each element is a GolferRoundScore object

    Algorithm:
    1. Create lookup maps ...
       a. Create a lookup map (golfer_name_to_id)
          for mapping golfer_name to golfer_id
       b. Create a lookup map (tourn_name_to_id)
          for mapping tourn_name to tourn_id

    2. Create an empty list called 'round_scores_list'
       that will be filled in with GolferRoundScore
       objects whose data comes from the input file
       and each of the object list parameters: golfers_list,
       tourns_list, rounds_list, tourn_golfers_list

    3. Initialize the golfer_scores_id

    4. Use a try/except block to capture a File Not Found Error
        a. Open the input file object for reading the input file
        b. Call the csv.reader function, passing in the input file
           and capturing the CSV file contents.
        c. Create a list from the file contents: 'golfer_scores_list'
        d. Close input_file object

    5. Create an outer loop to read each set of scores in 'golfer_scores_list'
       Outer Loop:
         a. Get the golfer_name, tourn_name, and day from the
            the first three elements, stripping whitespace.
         b. The rest of the elements (using slice scores[3:])
            are converted to a list of ints - scores_list.
            Use Python's 'map' function to convert the strings to ints 
            and then use the 'list' function to convert the object returned
            from the map to a list.
         c. Get the golfer_id using the golfer_name_to_id (from step 3a)
         d. Get the tourn_id using the tourn_name_to_id (from step 3b)
         e. Call helper functions to get round_id, and the tourn_golfer_id
         f. Set the total_round score by summing the scores_list
         g. Create a new GolferRoundScores object, call it golfer_scores,
            passing in golfer_scores_id, tourn_golfer_id, round_id,
            total_round_score, and the scores list (from step 5b.)
         h. Append the GolferRoundScores object to the round_scores_list
         i. Increment the golfer_scores_id
    6. Print the round_scores_list objects to the console
    7. Return the round_scores_list
    """

    print("\nThe GolferRoundScores object list\n")

    ### Please provide your code here        

    return round_scores_list


def get_tourn_golfer_id(tourn_golfers_list, tourn_id, golfer_id):
    """
    Helper function to get the tourn_golfer_id
    based on the specified tourn_id and golfer_id
    """

    for tourn_golfer in tourn_golfers_list:
        #    Loop looking for the TournGolfer object,
        #    tourn_golfer, whose golfer_id instance
        #    variable value matches the specified golfer_id
        #    and whose tourn_id instance variable value
        #    matches the specified tourn_id

        if tourn_golfer.get_golfer_id() == golfer_id:
            if tourn_golfer.get_tourn_id() == tourn_id:
                # a. When the matching TournGolfer object
                #    is found, return the tourn_golfer_id from
                #    the TournGolfer object, tourn_golfer

                return tourn_golfer.get_tourn_golfer_id()

    # tg not found - just return 0
    return 0


def get_round_id(rounds_list, tourn_id, tourn_day):
    """
    Helper function to get the round_id
    based on the specified tourn_id and tourn_day
    
    Loop looking for the Round object whose 
    tourn_id instance variable value matches 
    the specified tourn_id and whose 
    day instance variable value matches the specified day
        When the matching Round object is found, 
        return the round_id from the round object

    """
    ### Please provide your code here (See get_tourn_golfer_id)        


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
