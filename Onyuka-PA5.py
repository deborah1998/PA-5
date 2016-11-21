


import os
# Purpose: read in a file from the user and return it once they give one that exists
# Parameters: None
# Return: file_name
def file_reader():
    #ask user for input
    file_name = input("Please enter the file you would like to input: ")
    #if input is invalid ask again
    while not os.path.exists(file_name):
        file_name = input("Invalid Input! Please enter the file you would like to input: ")
    return file_name


#Function Name:read_file
#Purpose:read from the file
#Parameters:filename
#Return:earthquakes list


def read_file(filename):
    try:
        inputfile=open(filename,"r")
        list=[]
        earthquakes=[]
        for line in inputfile:
            list = line.strip().split(",")
            earthquakes.append(list)
        inputfile.close()
    except:FileNotFoundError
    print("Sorry this file is not Found")
    SystemExit(1)
    return earthquakes


def find_earthquakes_on_date(outfile_name,earthquakes):
    outputfile=open(outfile_name)
    earthquake_date=("Please enter a specific date in which the program will find all earthquakes for")
    for i in len(earthquakes):






    outputfile.close()


