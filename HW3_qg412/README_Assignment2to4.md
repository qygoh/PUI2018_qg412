# For Assignments 2,3&4

## Assignment 2

The main file for this assignment is _Assignment2_qg412_, which stores both the compulsory and extra credit assignment. 

### What I Did
 1) Searched NYCOpenData for a suitable data set.
 2) Used curl to download data for the compulsory section
 3) Used api to read json for extra credit section. 

### Groups and my contributions
I did assignment 2 in collaboration with Mark Bauer @mebauer and Yushi Chen @Amberchen724. 
For the extra credit assignment, Vaidehi shared with me how to sort the year in chronological order.  

## Assignment 3

The main file of interest for Assignment 3 is _show_bus_locations_qg412.py_, which if done correctly, will show the user real time bus locations in bus line B52 when queried in the terminal. 

### What I did 
1. Copied the basic structure of a python script from Prof Bianco's _aSimplePythonScript.py_
2. Added more stuffs to the python script from Prof Bianco's _APIreadingJson.ipynb_, but excluded import pylab as no mapping is required 
3. Edited the url to make it dynamic such that it can read different API keys for marking purposes
4. Spent a really long time trying to sieve out where the latitude and longtitude as well as their locations in the dictionaries
5. Wrote the code that will print the output correctly using a for loop as well as an iterator!

### Groups and my contribution
I am **extremely thankful** for Vaidehi, Kloe, Rachel Sim and Mei Guan for our almost daily (!) discussion sessions. 

I was mostly struggling to understand what is required of us to do the assignment and how to even do it cause there was no mention of how to create a python script at all in class. 

While my code was written independently, it was not possible without the guidance of my friends who showed me how they did it.

## Assignment 4

The main file of interest for Assignment 4 is _get_bus_info_qg412.py_, which if done correctly, will show give a csv file storing information about real time bus locations, stop name and stop status in bus line B52 when queried in the terminal. 

### What I did
1) Copy most part of the code from Assignment 3 except for the output portion
2) Identifed the dictionaries where Stop Name and Stop Status are located
3) Use for loop, iterators and booleans to be able to render output. Boolean is needed because stop name and stop status have "NA" values, which will break the entire code as it is not numerical. The way around is to do boolean what will ask system to print NA for such values, if not, move on. 
4) Adjust the code to be able to render the output in desired format in csv file

### Groups and my contributions
Having struggled through assignment 3, assignment 4 was more manageable! 

Vaidehi, Kloe, Rachel Sim shared their coding discussion about boolean with me, without which this entire assignment would not have been able to work at all! 

My produest achievement is being able to write most of the code that asks the system to write the output into csv files myself, with some help from Vaidehi who helped me troubleshoot a little when the codes failed due to syntax errors.  