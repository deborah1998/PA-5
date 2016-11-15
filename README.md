# CS201 PROGRAMMING ASSIGNMENT #5  
60  POINTS   (10pts design, 50pts final)  
DESIGN DUE: 11/16/16  
FINAL DUE: 11/22/16 (**TUESDAY**)

## PROBLEM 
Earthquakes hit all of the time; there are so many of them that it would be impossible to try to analyze them without the help of computers.  
You have access to earthquake data from the last 30 days.  What can you learn about the earthquakes using your programming knowledge?  
The data we are using originally came from http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

## PURPOSE OF THE ASSIGNMENT
The purpose of this assignment is to give you practice with

1. reading from a file
2. processing Strings
3. function design and implementation
4. error checking
5. using lists

## REQUIREMENTS ANALYSIS
The first stage in your programming assignment is the requirements analysis stage.  You need to make sure you understand the below requirements for what your program needs to do. 
First, you need to understand your data in quakes.csv. Your data is comma separated, like the movie data was in a prior lab.

Each line in the file contains:
* The date and time of the earthquake in the format year-month-dayThour:minute:secondsZ
* The latitude (-90 to 90)
* The longitude (-180 to 180)
* The depth at which the earthquake occurred (negative means below ground, positive means above)
* The magnitude (-1 to 10), a measure of the size of an earthquake at its source
* The dmin, a horizontal distance from the epicenter to the nearest station (in degrees). 1 degree is approximately 111.2 kilometers. In general, the smaller this number, the more reliable is the calculated depth of the earthquake.
* The id, a unique identifier for a particular earthquake
* The location where the earthquake occurred (text).
* The horizontal error (0 to 100), Uncertainty of reported location of the event in kilometers.
* The depth error (0 to 100), Uncertainty of reported depth of the event in kilometers.
* The magnitude error (0 to 100), Uncertainty of reported magnitude of the event; The estimated standard error of the magnitude.

Your program must work for any file of the above format, and should determine the following for the user:
* Output to a file (name given by the user) all earthquakes that occurred on a specific date (provided by the user).
 Should be in the same format as the original input file.
* Output to the user the average magnitude of the earthquakes in the file
* Output to the user the number of earthquakes within
 a specific distance of a specific location. Distance is given by user as kilometers,
 and location is given by user as a latitude and longitude. You must calculate a distance between 2 points based on latitude and longitude.
  The shortest distance between two given points P1=(lat1, lon1) and P2=(lat2, lon2) can be calculated using the formula distance
  = arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)) * 6371. Note that one of these points comes from the file,
  and one of these points comes from the user, and if you just copy/paste this equation into Python it WILL NOT work.
  See requirements below about programming.

Your program must allow the user to choose which of the above options they want to do, and after completing the chosen option, must allow the user to choose another option or choose to end the program.

Your program should have good error checking so that it doesn't crash. Some examples you need to consider: file name checking, try/except in file processing functions, and checking that input by the user is appropriate for the data they are supposed to be inputting (type or value).

## DESIGN
The second stage is to design your solution based on the requirements:

1. Determine the tasks being accomplished in your program. 
2. Write an algorithm for each function. This algorithm includes parameters, calculations, and returned values. This algorithm should include your personally designed question.
3. Double check that you included all of the requirements, and appropriate error checking.

*NOTE:* There are no aspects of this design/code that you can google how to solve. The only appropriate googling will be if you want to understand more about earthquake data, or are looking up a specific Python module.

**DESIGN SUBMISSION: 11/16/16**
Submit to GitHub: your algorithm for your program in designInitial.txt, following the format we've been using.

***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.


## PROGRAMMING REQUIREMENTS
After your design is complete and correct, it’s time to start programming and then testing:

* Fix design issues: If there were issues with your design, either not meeting requirements or in the format, fix that before you start writing your code.
* Implementation: Write your program following the requirements and based on your design.
  * Follow good usability/HCI principles in your input and output (make it clear the type of input you are asking for)
  * Follow good use of functions
  * Remember to define functions before they are used (so if function A calls function B, you need to define function B first in your program)
  * Remember to state the purpose of the program
  * Follow iterative development to make your life easier. Make sure you correctly read in and store the data. Then implement ONE question, and get that working. Then worry about adding in the next question. New questions shouldn't stop old questions from working, but should only add on to it.
  * To program the final question, you will need to use the math module. You should look up what each of the functions you need is called in the math module, and modify the equation to work in Python.
  * You may find using the sep and end parameters for the print function useful for your output formatting. You can read about them in your book or look them up online.
* Testing: Make sure it works correctly; give it sample input, and check that the output is correct.
  * Create a test file that contains at most 10-15 lines from the original file, or make up your own data in the same format. Name it testinput.txt. Create a set of test cases based on this test file (1 case per question). If you have a representative set of 10 lines, then if it works on this file then it *probably* works on the real file. This is a standard way to test file code, because it makes it easier to figure out the right answer.
  * Test your program using the test cases. Also test all error checking. Make sure it seems to work with the full file as well.

## ASSIGNMENT REMINDERS
Follow the programming assignment requirements document for comments, formatting, etc. You must use a list to store data from a file, and then process that data in other functions.

Recall that you may not do someone else’s work, or have someone else do your work. Sharing of solutions is an honor code violation. This includes someone who is not in the class, including a tutor, writing any or all of your algorithm or code or dictating to you how to do it. As everyone in the class is solving the same problem, no code may change hands. See the syllabus for details or ask the professor if you are unsure.

## EXTRA CREDIT 
Create an additional question for your program to solve, and incorporate it into your code. The more impressive, the more extra credit (up to 2 points). *Describe in extracredit.txt the question you are answering, and what function it is calculated in (keep it brief).*

## REFLECTION
Write a short reflection about the programming assignment in reflection.txt: what did you learn, what would you do differently next time, what was difficult, what do you like/dislike about working with files/functions/lists?  This should be no more than a page.

## FINAL SUBMISSION   
* To GitHub:
  * Your .py file
  * A brief description in extracredit.txt as described above, if applicable
  * Your reflection of the programming assignment in reflection.txt
  * Your test cases in testcases.txt.
  * Your test file in testinput.txt
  * Note: You are not required to turn in an updated algorithm for this PA
* Hardcopy in class:
  * A printout of your .py file

***Remember to double check on github.com that your files pushed. If they didn’t, you need to push them. I can only see what is on github.com, not what is only on your computer.


