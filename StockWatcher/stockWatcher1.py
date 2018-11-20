import sys, time
import requests, bs4
import threading, logging
import smtplib
from random import *
from twilio.rest import Client

# constants used
WAIT_INTERVAL = 120
LOG_FILE = 'stockPriceLog.txt'
SMTP_HOST = 'smtp.gmail.com'
SMTP_TLS_PORT = 587

def main():
    """
    Clear the log, set up logging, log a start message
    Retrieve the list of stock symbols from the command line
    Start up a thread for each stock listed
    Sleep a little to allow the stock prices to be logged
    Have the user enter CTRL-C to stop the program.
    """
    open (LOG_FILE, 'w').close()
    logging.basicConfig (filename=LOG_FILE,
    level=logging.INFO,
    format=' %(asctime)s %(message)s ')
    logging.info ("StockWatcher - start program")
    # For Stage 2: Add in CODE HERE to get the
    # stock symbols from the command line,
    # instead of using the hardcoded list
    stock_list = sys.argv[1:]
    for i in range (len (stock_list)):
        stock = stock_list[i].upper()
        print ("Begin watch for " + stock)
        thread = threading.Thread (target=getQuote,
        args= (stock, ))
        thread.start()
    time.sleep (5) # Sleep for threads print msgs
    input ("\nHit CTRL-BREAK to stop recording.\n\n")
    logging.info ("StockWatcher - end program")

def getQuote (symbol):
    """
    Get a stock quote for the given stock symbol using
    Python requests and BeautifulSoup modules.
    Determine the availability of webpage
    Request the quote every 10 minutes until the user ends
    the program with CTRL-C
    Compare current quote with previous quote and send
    text when different.
    """
    # For Stage 3: Replace CODE HERE to get the stock
    # prices from the Yahoo Finance website using
    # requests and Beautiful Soup, instead of
    # using the hardcoded list
    prices = ['20', '25', '30', '30', '30', '20']
    price = prices[0]
    prevPrice = '10'
    text = "Start watching " + symbol + ": Price: " + str (price)
    print (text)
    logging.info (text)
    i = 0 # not needed with Stage 3 and 4
    # Start watching and continue until CTRL-Break
    while True:
        # Get Price with Stage 1 and 2 only
        # Stage 3 and 4 uses requests and Beautiful Soup
        price = prices[i%6]
        # Send price for symbol to log
        logging.info (symbol + "\t" + str (price))
        i = i + 1 # not needed with Stage 3 and 4
        # Check for price difference and send text,
        # if different
        if price != prevPrice:
            text = symbol + " now at " + str (price) + \
            "; was " + str (prevPrice)
            print (text)
            sendTextMsg(text)
            sendEmail(text)
            prevPrice = price
        time.sleep (WAIT_INTERVAL)

def sendTextMsg(msg):
    """
    For now, this program just prints a message
    The code that sends the text message is in Stage 4
    """
    print ("sendText: " + msg)

def sendEmail(msg):
    """
    For now, this program just prints a message
    The code that sends the email is in Stage 4
    """
    print ("sendEmail: " + msg)
main()
