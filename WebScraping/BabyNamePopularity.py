"""
This program uses selenium and BeautifulSoup to
Navigate thru the Social Security Administration website
and scrape the pages for the average rank in popularity
of a given name for the years 2000 - 2016

FireFox -
    browser 56.0  (64-bit)
    driver geckodriver-v0.20.1 (64bit)  

Chrome -
    browser 64.0.3282.186 (64-bit)
    driver chromedriver 2.37  (There is only a 32bit version )

the drivers must be in the path

"""

import sys
# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def main():
    # A.
    # get a list of names to display
    # babynames = []
    count = 0
    # check len(sys.argv) to make sure at least one name was entered
    # remember, sys.argv[0] is the program name, so there is always at least one paramenter
    # if no parameters are entered print the following and return
    #      print("Syntax: python BabyNamePopularity.py babyname babyname ...")

    # HINT to get the list of names use [1:] on the sys.argv list
    # babynames = sys.argv[0]
    babynames = sys.argv[1:]
    count = len(babynames)
    if count is 0:
        print("Syntax: python BabyNamePopularity.py babyname babyname ...")
        return

    # B.
    # setup the driver and launch - either Chrome or FireFox
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    # the page to get is ("https://www.ssa.gov/OACT/babynames/index.html")
    driver.get("https://www.ssa.gov/OACT/babynames/index.html")
    print(driver.title)

    # C.
    # loop for each name in the babynames list, print the name and
    # call the printNameRanking method passing in the driver and the name
    for babyname in babynames:
        print(babyname)
        printNameRanking(driver, babyname)

    # close the driver and return
    # driver.close()
    driver.quit()

def printNameRanking(driver, babyname):
    """
    Using the driver, scrape the SSA website for the popularity of babyname.
    
    """

    # 1. create a  'wait' object for waiting for 10 seconds for pages to load
    wait = WebDriverWait(driver, 10)

    # 2a. Use a try/except block to capture a TimeoutException
    try:
        # a. use wait.until presence of element located to wait for the "name" element.
        elem = wait.until(EC.presence_of_element_located(
            (By.ID, "name")))
        # b. clear the form
        elem.clear()
        # c. use send_keys() to enter the babyname
        elem.send_keys(babyname)
        # d. get an object for use the Select method with find_element_by_id("start")
        years = Select(driver.find_element_by_id("start"))
        # e. select_by_value("1960")
        years.select_by_value("1960")
        # f. submit the form
        elem.submit()
    # 2b. add the except for the TimeoutException,
    except TimeoutException:
        # a  print an error message
        print("Locating Baby Name Field Failed")
        # b  return
        return

    # Wait for the next page -- See the TopBabyNames program ...
    # 3a. Use another try/except block to capture a TimeoutException
    # a. wait for next page, which has a link named "Popular baby names"
    # 3b. add the except for the TimeoutException,
    # a. print an error message,
    # b. go back one page
    # c. return
    try:
        elem = wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Popular baby names")))
    except TimeoutException:
        print("Next page not loaded")
        driver.back()
        return

    # 4. use BeautifulSoup to create a 'soup' object for parsing the values on the page
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 5. get the list of tables - use findChildren('table')
    # tables = soup.findChild('table', {'summary': "formatting" })
    tables = soup.findChildren('table')

    # create some variables to hold the data ...  
    ranks = []
    bestRank = 999
    yearsOfBestRank = []
    # each rank is stored in it's own table, one row per table
    # not sure why,  but strategy is to loop through all the tables
    # and find any table with a row that has "20xx" or "19xx" as its first column
    # The second column will be the rank for that year

    # 6. Loop, for each table in the table list:
    for table in tables:
        #  a. Get the first and only row, using findchild('tr')
        # Get all the rows
        rows = table.findChild('tr')
        # rows_first = rows[0]
        #  b. Get the columns using findChildren('td')
        columns = rows.findChildren('td')
        # parse data from columns
        #  c. If there are columns and there are at least 2 of them
        if columns is not None and len(columns) >= 2:
            #  c1. get the year (first column) , don't forget to strip whitespace
            year = columns[0].getText().strip()
            # c2. If the year starts with "20" or "19"
            #if year == "20**" or year == "19**":
            #if "20**" in year or "19**" in year:
            if year.startswith('20') or year.startswith('19'):
                #  c2a. get the ranking (second column) , don't forget to strip whitespace
                rank = int(columns[1].getText().strip())
                #  c2b. append the rank to the ranks list
                ranks.append(rank)
                #  c2c. if rank is lower than or equal to the bestRank:
                if rank <= bestRank:
                    #  c2c1. if lowest so far, clear the yearsOfBestRank, since new best has been found
                    # rank_lowest = min(bestRank)
                    if rank < bestRank:
                        yearsOfBestRank.clear()
                    #  c2c2. append this year to the yearsOfBestRank list
                    yearsOfBestRank.append(year)
                    #  c2c3. reset bestRank to the current rank
                    bestRank = rank
    # 7. if the ranks list is not empty,
    if len(ranks) > 0:
        # a. display the average
        print("Avg ranking for {}: {}".format(babyname, sum(ranks) / len(ranks)))
        # b. display years of best ranking
        print("Best ranking was {}, in {} \n".format(bestRank, yearsOfBestRank))

    # 8 else print a message that no data was found
    else:
        print("Could not find data.")

    # 9. go back to the previous page
    driver.back()

# main
try:
    main()

except:
    print("Caught exception running program.")
