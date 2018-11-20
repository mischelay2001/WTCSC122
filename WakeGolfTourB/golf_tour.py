
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
    1. Create a lookup dictionary that contains the golf_course_name
       as the key and the golf_course_id as the value using the
       GolfCourse objects passed in the golf_course_list:
       Code is provided in the Project1B doc.
    2. a. Create an empty list called tournament_list
          that will be filled in with tournament objects
          created in this function from the input file data.
       b. Create an empty tourn_golfer_dict dictionary that
          will contain the tournament id as the key and the 
          list of golfers as the value. The loop below
          will fill in this dictionary value list, when
          each golfer name is read in.
    3. Initialize the tourn_id to 1 and the tourn_id_key to 0
    4. Use a try/except block to capture a File Not Found Error
        a. Open the input file object for reading the input file.
        b. Call the csv.reader function, passing in the input file
           and capturing the CSV file contents.
        c. Create a list from the file contents: tournament_input_list
        d. Create a loop to traverse the tournament_input_list,
           where the loop variable 'tourn_info' will contain either the
           tournament information, or a golfer name.
           Loop:
           1. Check the length of tourn_info, if it is one, then it is a
              golfer name, so add it to the tourn_golfers_dict value list.
              It will be used later in the create_tourn_golfers method.
              a. Get the golfer name from tourn_info stripping whitespace
              b. Add the golfer name to the tourn_golfers_dict value
           2. If the length is greater than one, then process the tournament 
              information
              a. Get each of the first five elements of the tourn inner list:
                 Strip - course_name, tourn_name, start_date,
                 Convert num_rounds and num_golfers to ints.
              b. Get golf_course id from lookup dictionary created above
              c. Create a new Tournament object, call it tournament,
                 passing in tourn_id, tournament_name, golf_course_id,
                 start_date, num_rounds, and num_golfers
              d. Append the tournament object to the tourns_list
              e. Set the tourn_id_key to tourn_id
              f. Create dictionary entry value for this tourn_id_key, 
                 the value is an empty list to be filled in later with 
                 the golfer names as they are read from the input file. 
              g. Increment the tourn_id

        e. Close the input file
    5. Print the tournament_list objects to the console
    6. Return the tournament_list and tourn_golfers_dict
    """
    print("\nThe Tournament object list:")

    ### create_tournaments function; author: Michele Johnson

    # Declare variables
    golf_course_name_to_id = dict() # dictionary; key: course name, value: course ID
    golf_course_id = 0              # golf course ID from golf course name to ID lookup map

    csv_delimiter = ','             # delimiter character in input data lines
    tournament_input_list = []      # list to hold all raw data from input file
    tournament_info = []            # list to hold only tournament info rows from input file
    tournament_rows =[]             # list of tournament rows

    tourn_id = 1
    tourn_id_key = 0

    golfer_names = []
    value_golfer_name = ""

    tourn_golfers_dict = dict()     # dictionary; key: tournament ID, value: list of golfers

    # Lookup map: course name to course ID
    for golf_course in golf_course_list:
        golf_course_name_to_id[golf_course.get_course_name()] = golf_course.get_course_id()

    # Get data from input file and store in list; tourn_input_list
    try:

        a_file = open(filename, 'r')
        row = csv.reader(a_file)

        # loop through each row of data
        for row in a_file:
            row = row.strip()
            tournament_input_list.append(row)

        a_file.close()
    except IOError:
         print("File Not Found Error.")

    count_rows = 0
    # Find all the tournament info rows
    for tournament_row, row_data in enumerate(tournament_input_list, 1):
        tourn_info_data = row_data.split(",")
        if len(tourn_info_data) > 1:
            # Add the row number to the tournament_rows list
            tournament_rows.append(tournament_row)
            # Add row number to the first position of info data
            tourn_info_data.insert(0, tournament_row)

            # Split and assign into variables for tournament info lines
            tourn_id = tourn_info_data[0]
            tournament_course_name = tourn_info_data[1].strip()
            tournament_name = tourn_info_data[2].strip()
            start_date = tourn_info_data[3].strip()
            round_number = tourn_info_data[4]
            golfer_amount = tourn_info_data[5]

            # Add the row data to the tournament_info list
            count_rows += 1
            tourn_info_data = count_rows, tourn_id, tournament_course_name, tournament_name, start_date, round_number, golfer_amount
            tournament_info.append(tourn_info_data)

            # Lookup tournament course name and return golfer course ID
            for course_name in golf_course_name_to_id:
                if course_name == tournament_course_name:
                    golf_course_id = golf_course_name_to_id[course_name]

    # Add last row number of input file to the last position of info data
    tournament_rows.append(len(tournament_input_list))

    # Loop through tournament row numbers
    # For current line of tournament info; look up corresponding tournament row number
    last_row = len(tournament_input_list)
    last_index = len(tournament_rows)-1
    row_between_counter = 0
    next_index = 0
    difference = 0

    try:
        while row_between_counter < last_index:
            tr = 0
            for tr in tournament_rows:
                # Second index; tournament row
                next_index = tournament_rows[row_between_counter + 1]
                # First index; tournament row
                current_index = tournament_rows[row_between_counter]
                # Assign first index to current row number; used to index tournament input rows
                current_row_number = current_index
                # Find the number of rows between the second index and first row of batch
                difference = next_index - current_row_number - 1
                # If second element of tournament info matches current_index
                row_between_counter += 1

                # If second element of tournament info does not match current_index
                if row_between_counter == last_index:
                    break

                tourn_golfers_dict[tr] = []
                for d in range(difference):
                    tourn_golfers_dict[tr].append(tournament_input_list[current_row_number])
                    current_row_number += 1
                golfer_names.clear()

        tr = tournament_rows[last_index-1]

        if row_between_counter >= last_index:

            # First index; tournament row
            current_index = tournament_rows[last_index-1]

            # Assign first index to current row number; used to index tournament input rows
            current_row_number = current_index

            # Find the number of rows between the second index and first row of batch
            difference = next_index - current_row_number
            # If second element of tournament info matches current_index
            row_between_counter += 1

            for d in range(difference):
                golfer_names.append(tournament_input_list[current_row_number])
                tourn_golfers_dict[tr] = golfer_names
                current_row_number += 1

    except IndexError:
        pass


    row_between_counter += 1

    new_dict = {}
    new_key = 1
    for k, nd in tourn_golfers_dict.items():
        new_dict[new_key] = nd
        print(new_key, new_dict[new_key])
        new_key += 1

    tourn_golfers_dict = {}
    tourn_golfers_dict = new_dict

    tournament_list = []

    # print("\nTournament Rows Numbers")
    # for tr in tournament_rows:
    #     print(tr)

    # print("\nTournament Row Data")
    # for ti in tournament_info:
    #     print(ti)

    # print("\nGolfer Names")
    # for gn in golfer_names:
    #     print(gn)

    # print("\nTournament Golfer")
    # print("List of keys ", tourn_golfers_dict.keys())
    # for k, tgd in tourn_golfers_dict.items():
    #     print(k, tgd)

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

    ### create_rounds function; author: Michele Johnson

    rounds_list = []
    round_id = 0
    num_rounds = 0
    day = ""

    # outer loop of tournament list
    for row_tourn in range(len(tournament_list)):

        tourn_data = str(tournament_list[row_tourn])

        tourn_data = tourn_data.split(",")
        round_number = int(tourn_data[4])
        tourn_id = int(tourn_data[0])

        num_rounds = round_number

        # inner loop
        for i in range(round_number):
            if num_rounds == 4:
                day = "Thu"
            elif num_rounds == 3:
                day = "Fri"
            elif num_rounds == 2:
                day = "Sat"
            elif num_rounds == 1:
                day = "Sun"
            num_rounds -= 1
            round_id += 1

            a_round = Round(round_id, tourn_id, day)
            rounds_list.append(a_round)

    # loop through tournament_list and print
    for g in rounds_list:
        print(g)

    return rounds_list


def create_tourn_golfers(tourn_golfers_dict,  golfer_list):
    """
    Use the tourn_golfers_dict, that was
    returned from the create_tournaments function, which contains
    entries with the key being the tourn_id, and the valus is a list following format:
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
    
    ### create_tourn_golfers function; author: Michele Johnson

    tourn_golfers_list = []
    tourn_golfer_id = 0
    
    golfer_name_to_id = dict()

    for course in golfer_list:      
        golfer_name_to_id[course.get_golfer_name()] = course.get_golfer_id()

    print(tourn_golfers_dict)
    for tourn_id, row_golfer_list in tourn_golfers_dict.items():

        for golfer_list_data in row_golfer_list:
            print(golfer_list_data)
            golfer_list_id = golfer_name_to_id[golfer_list_data]
            print(golfer_list_id)

            tourn_golfer_id += 1
            a_tournament_golfer = TournGolfer(tourn_golfer_id, tourn_id, golfer_list_id)
            tourn_golfers_list.append(a_tournament_golfer)

    for g in tourn_golfers_list:
        print(g)

    return tourn_golfers_list


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
