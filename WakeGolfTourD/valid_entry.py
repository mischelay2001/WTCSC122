__author__ = 'Michele Johnson'

def integer_entry(a_request_text):
    # Check input is valid
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value
    entry = ""
    while is_entry_valid is False:
        try:
            entry = int(input(a_request_text + ":\t"))
            is_entry_valid = True

        # Invalid entry error handling and message
        except ValueError:
            pass
            print("\nInvalid Entry\n")
    return entry


def float_entry(a_request_text):
    # Check input is valid
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: float
    entry = ""
    while is_entry_valid is False:
        try:
            entry = float(input(a_request_text + ":\t "))
            is_entry_valid = True

        # Invalid entry error handling and message
        except ValueError:
            pass
            print("\nInvalid Entry\n")
    return entry


def alpha_entry(a_request_text):
    # Check input is valid
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: alphabetic string
    entry = ""
    while is_entry_valid is False:
        entry = str(input(a_request_text + ":\t "))
        # Clean unwanted characters
        entry = entry.strip()
        clean_chr = ["(", ")", "-", "."]
        for i in clean_chr:
            entry = entry.replace(i, "")
        # Check for validity all alphabetic
        is_alpha = entry.isalpha()
        if is_alpha is False:
            # Output to display
            print("\nThe entry is not a valid.\n")
        else:
            entry = entry.title()
            is_entry_valid = True
    return entry


def clean_string_digits(a_request_text, digit_length):
    # Check input is valid
    # Function to obtain valid entry per program requirements
    # Will ask user for input per program requirements
    # Will return an error message if entry is invalid

    # Initiate test variable to false
    is_entry_valid = False
    # Initiate entry variable to match correct variable type and value: string
    entry = ""
    while is_entry_valid is False:
        entry = str(input(a_request_text + "\t"))
        # Clean unwanted characters
        entry = entry.strip()
        clean_chr = ["(", ")", "-", ".", " "]
        for i in clean_chr:
            entry = entry.replace(i, "")
        # Check for validity digits
        is_digit = entry.isdigit()
        entry_length = len(entry)
        if (is_digit is False) or (entry_length != digit_length):
            # Output to display
            print("\nThe entry is not a valid.\n")
        else:
            is_entry_valid = True
    return entry


def clean_date_yyyymmdd(entry):
    # Function to clean and convert m/d/y to yyyy/mm/dd format

    # entry = input("Raw date")

    # Clean unwanted spaces and characters
    entry = entry.strip()
    clean_chr = ["(", ")", "\\", ".", ",", " "]
    for i in clean_chr:
        entry = entry.replace(i, "")

    # Ensure only / is the delimited character
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
        elif 9 < date_year <= 18:
            date_year = "20" + str(date_year)
        elif 19 < date_year <= 99:
            date_year = "19" + str(date_year)

    # Convert date into yyyy/mm/dd format
    entry = (str(date_year) + "/" + str(date_month) + "/" + str(date_day))

    return entry


def clean_birthdate_yyyymmdd(entry):
    # Function to clean and convert m/d/y to yyyy/mm/dd format

    # entry = input("Raw date")

    # Clean unwanted spaces and characters
    entry = entry.strip()
    clean_chr = ["(", ")", "\\", ".", ",", " "]
    for i in clean_chr:
        entry = entry.replace(i, "")

    # Ensure only / is the delimited character
    date_chr = ["/", "-"]
    for i in date_chr:
        entry = entry.replace(i, "/")

    # Separate into month, day, year
    entry = entry.split("/")
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
    entry = (str(date_year) + "/" + str(date_month) + "/" + str(date_day))

    return entry
