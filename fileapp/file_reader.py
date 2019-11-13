"""
File Reader for Airports
"""
import sys
from utils import check_exists
from mail_sender import send_confirmation

# declaration
AIRPORTS = []
# declaration
SM_AIRPORTS = []

# function read _data


def read_data(file_name):
    """
    Read The  File
    """
    file = open(file=file_name, mode='r', encoding='utf-8')
    if file:
        line = file.readline()
        while line:
            AIRPORTS.append(line)
            line = file.readline()
        print("Total Airports in the file ")
        print(len(AIRPORTS)-1)


def parse_data():
    """
    Parse the data
    """
    for airport in AIRPORTS:
        airport = airport.replace('"', '')
        cols = airport.split(",")
        if cols[2] == 'small_airport':
            SM_AIRPORTS.append(cols[3])
    sorted_airports = sorted(SM_AIRPORTS, reverse=False)
    send_confirmation(len(SM_AIRPORTS), "nilesh.devdas@vinsys.com")


def read_file():
    """
     load the file
    """
    file_name = sys.argv[1]
    if check_exists(file_name):
        print("Reading File")
        read_data(file_name)
        parse_data()
    else:
        print("File may not exist so check")


read_file()
