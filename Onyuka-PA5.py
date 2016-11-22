



import math
import os
# Purpose: read in a file from the user and return it once they give one that exists
# Parameters: None
# Return: file_name
def file_reader():
    #ask user for input
    file_name = input("Please enter the file you would like to input:")
    #if input is invalid ask again
    while not os.path.exists(file_name):
        file_name = input("Invalid Input! Please enter the file you would like to input: ")
    return file_name


#Function Name:read_file
#Purpose:read from the file
#Parameters:filename
#Return:earthquakes list


def read_file(file_name):
    try:
        inputfile=open(file_name,"r")
        earthquakes=[]
        for line in inputfile:
            earthquakes.append(line.strip().split(","))
        inputfile.close()
    except FileNotFoundError:
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
    earthquake_date=(year+"-"+month+"-"+day)
    for i in range (len(earthquakes)):
        if earthquake_date == earthquakes[0]:
            print(earthquakes[0:9], file =outputfile)
            outputfile.close()



#Function Name:average_magnitude
#Purpose:find the average of the earthquakes in the file
#Paramaters: the list earthquakes
#Return:average magnitude of earthquakes in file

def average_magnitude (earthquakes):
    total=0
    count=0
    for i in range(len(earthquakes)):
        total=float(total+int(earthquakes[i][4]))
        count+=1
        average = total/count
        return average


#Function Name:num_of_earthquakes_in_distance
#Purpose:To find the number of earthquakes within a specific distance of a specific location
#Paramaters: the list earthquakes
#Return:number of earthquakes within the distance of a specific location

def num_of_earthquakes_in_distance(earthquakes,lat1,lon1,user_distance ):
    count=0
    for i in range(len(earthquakes)):
        distance =float(math.acos(math.sin(lat1) * math.sin(earthquakes[1]) + math.cos(lat1) * math.cos(earthquakes[1]) * math.cos(lon1 - earthquakes[2])) * 6371)
        if distance <= user_distance:
            count+=1
    return count


#Function Name:Menu
#Parameters:None
#Return:chosen menu option

def menu():
    print("The choices you have to choose from to learn more about earthquakes is dates, magnitude, and distance")
    choice = input("What would you like to know about earthquakes?")
    return choice



#Function Name:main
#Purpose:run the overall program
#Paramaters:none
#Return:none


def main():

    print("The purpose of this program is to analyze earthquake data based on your choice")
    inputfile=file_reader()
    new_list =read_file(inputfile)
    choice=menu()
    if choice.lower() == "dates":
        outputfile = input("Please enter the name of the output file:")
        find_earthquakes_on_date(new_list,outputfile)
    if choice.lower() =="magnitude":
        avg_mag=average_magnitude(new_list)
        print("The average magnitude of the earthquakes",avg_mag)
    if choice.lower() == "distance":
        lat1 = float(input("Please enter a specific latitude: "))
        while lat1 < -90 or lat1 > 90:
            print("This is ivalid input!")
            lat1 = float(input("Please enter a specific latitude: "))
        lon1 = float(input("Please enter a specific longitude:"))
        while lon1 < -180 or lon1 > 180:
            print("This is invalid input!")
            lon1 = float(input("Please enter a specific longitude:"))
        user_distance = ("Please enter a specific distance:")
        num_distance = num_of_earthquakes_in_distance(new_list, lat1, lon1, user_distance)
        print("The number of earthquakes within that distance is",num_distance)
        choice2 = input("Would you like to choose another option?")
        while choice2.lower == "yes" and choice2.lower!= "no":
            input("Would you like to choose another option?")
            choice2=menu()


main()












