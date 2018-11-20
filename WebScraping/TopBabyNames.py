"""
This program uses selenium and BeautifulSoup to
Navigate thru the Social Security Administration website
and scrape the pages for a list of top baby names for
the years 2010 - 2016

FireFox -
    browser 53.0.3  (64-bit)
    driver geckodriver-v0.16.1 (64bit)  (v17 is broken, at least for me)

Chrome -
    browser 59.0.3071.86 (64-bit)
    driver chromedriver 2.29 (I could only find the 32bit version but it worked for me

the drivers must be in the path

"""
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def main():

    # set driver and launch webpage
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver.get("https://www.ssa.gov/OACT/babynames/index.html")
    # print (driver.title)

    years = ['2016', '2015', '2014', '2013', '2012', '2011', '2010']
    num_of_names = 5
    for year in years:
        print(year)
        printMostPopularNames(driver, year, num_of_names)

    driver.quit()

def printMostPopularNames(driver, year, num_of_names):

    # find the form for submitting the year, clear it, add the year and submit
    wait = WebDriverWait(driver, 10)
    try:
        elem = wait.until( 
            EC.presence_of_element_located((By.ID, "year")))
        elem.clear()
        elem.send_keys(year)
        elem.submit()

    except TimeoutException:
        print("Locating year field Failed")
        return

    # wait for next page
    try:
        elem = wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "Popular baby names")))
    except TimeoutException:
        print("Next page not loaded")
        return

    # use soup to parse values
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # get the names table ...
    table = soup.findChild('table', {'summary':'Popularity for top 20'})
    if table is not None:

        boyNames = []
        girlNames = []
        # Get all the rows
        rows = table.findChildren('tr')
        for row in rows:
            columns = row.findChildren('td')
            # parse data from columns
            # column 0, is the rank, column 1 is the boys name, column2 is the girls name
            if columns is not None and len(columns) > 2:
                boyNames.append(columns[1].getText().strip())
                girlNames.append(columns[2].getText().strip())

            # break out of loop after we have the requested number of names
            if len(boyNames) == num_of_names:
                break

        # display the names
        print("Boy  Names: ",boyNames)
        print("Girl Names: ",girlNames)

    else:
        print("Could not find data.")

    # go back to the previous page
    driver.back()

# main
try:
    main()
except:
    print("Caught exception running program.")
