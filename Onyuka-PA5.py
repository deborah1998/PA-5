


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

#Function Name:find_earthquakes_on_date
#Purpose: find and output to a file all earthquakes that occured on a specific date
#Parameters:the list earthquakes,outfilename
#Return:none


def find_earthquakes_on_date(outfile_name,earthquakes):
    outputfile=open(outfile_name)
    print("")
    month=input("Please enter a specific month(two digits)")
    day=input("Please enter a specific day(two digis)")
    year=input("Please enter a specific year(four digits)")
    earthquake_date=(month+"-"+day+"-"+year)
    for i in range (len(earthquakes)):
        if earthquake_date == earthquakes[0]:
            print(earthquakes[0:9])
        else:
            print("This is an invalid date")
    outputfile.close()

#Function Name:average_magnitude
#Purpose:find the average of the earthquakes in the file
#Paramaters: the list earthquakes
#Return:average magnitude of earthquakes in file

def average_magnitude (earthquakes):















