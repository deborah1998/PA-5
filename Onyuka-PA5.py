import math
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
            earthquakes[0].split["T"]
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
    outputfile=open(outfile_name,"w")
    month=input("Please enter a specific month(mm)")
    day=input("Please enter a specific day(dd)")
    year=input("Please enter a specific year(yyyy)")
    earthquake_date=(month+"-"+day+"-"+year)
    for i in range (len(earthquakes)):
        if earthquake_date == earthquakes[0][0]:
            print(earthquakes[0:9], file =outputfile)
        else:
            print("This is an invalid date!")
    outputfile.close()

#Function Name:average_magnitude
#Purpose:find the average of the earthquakes in the file
#Paramaters: the list earthquakes
#Return:average magnitude of earthquakes in file

def average_magnitude (earthquakes):
    total=0
    count=0
    for i in range(len(earthquakes)):
        total=float(total+earthquakes[i][4])
        count+=1
        average = total/count
        return average


#Function Name:num_of_earthquakes_in_distance
#Purpose:To find the number of earthquakes within a specific distance of a specific location
#Paramaters: the list earthquakes
#Return:distance calculation

def num_of_earthquakes_in_distance(earthquakes,lat1,lon1 ):
    for i in range(len(earthquakes)):
        distance =(math.acos(math.sin(lat1) * math.sin(int(earthquakes[1])) + math.cos(lat1) * math.cos(earthquakes[1]) * math.cos(lon1 - earthquakes[2])) * 6371)
    return distance


def menu():
    print("The  choices you have to choose from to laern more about earthquakes is dates, magnitude, and distance")
    choice = input("What would you like to know about earthquakes?")
    if choice.lower == "dates":
        find_earthquakes_on_date(ear)
    if choice.lower =="magnitude":
        average_magnitude()
    if choice.lower == "distance":
        num_of_earthquakes_in_distance()
















