MVal
March 4, 2023   
IT FDN 110 A  
Assignment07 Part II  
 

# Assignment 07 - Pickling and Error Handling in Python 

Pickle is a module that is specific to Python used for binary serialization and deserialization of Python
Objects (that means that it is converting objects into 0s and 1s). Things that can be pickled include  integers, strings, lists, functions and many more. In Python, pickling objects are serialized into a non-human readable format. Use cases for pickling include are: storing into byte streams in files, databases and for moving data across the network. It is key to understand that Pickled objects are not inherently  secure or encrypted, users should be aware that malicious data can be constructed to be executed during the unpickling process. This means users should only unplickle trusted data sources.  
How to pickle in Python 
To pickle in Python, first thing to do is use the “import pickle” to import the module. We can then use pickle.dump and ‘wb’ to save binary data to a file object, in the example in figure 1, we are saving this to a binary. From figure 2, we can see what a binary file looks like, its representation cannot be interpreted by humans but computers have no problem understanding 0s and 1s. 

## How to pickle in Python 
To pickle in Python, first thing to do is use the “import pickle” to import the module. We can then use pickle.dump and ‘wb’ to save binary data to a file object, in the example in figure 1, we are saving this to a binary. From figure 2, we can see what a binary file looks like, its representation cannot be interpreted by humans but computers have no problem understanding 0s and 1s. 

```
# ------------------------------------------------- #
# Title: Pickle Example 1
# Description: How to store data in a binary file
# ChangeLog: (Who, When, What)
# MValencia,3.4.2023,Created Script
# ------------------------------------------------- #


import pickle
dicRow = {"Task: Clean", "Priority: Low"}
file_name = "MyFile.dat"


objFile = open(file_name, 'wb')
pickle.dump(dicRow, objFile)
objFile.close()
```
Figure 1 - Pickle to File  

![Screenshot 2023-03-05 at 4 19 16 PM](https://user-images.githubusercontent.com/125417260/222994557-ec63bf91-7990-434a-a131-bfb50643e7c1.png)  
Figure 2 - Saved Binary FIle

## Unpickle Data from a file 
To unpickle data, in other words to make it human readable we can use the ‘pickle.load’ and ‘rb’ module to read the picked object from the file object, in the example below in figure 3 we are reading from a binary file. Figure 2 we can see that we now can understand the objects saved in the binary file by unpickling: 

```
# ------------------------------------------------- #
# Title: Pickle Example 1
# Description: How to store data in a binary file
# ChangeLog: (Who, When, What)
# MValencia,3.4.2023,Created Script
# ------------------------------------------------- #
import pickle
dicRow = {"Task: Clean", "Priority: Low"}
file_name = "MyFile.dat"


objFile = open(file_name, 'rb')
objFileData = pickle.load(objFile)
objFile.close()


print(objFileData)
```
Figure 3 - Unpickle from a file  

![Screenshot 2023-03-05 at 4 20 41 PM](https://user-images.githubusercontent.com/125417260/222994652-644de93a-a42e-42dd-91ef-6c718c4001c9.png)  
Figure 4  - Unpickled Data


## Pickle a List in a Function 
A more complex example in figure 5, we are pickling within a function with pickle.dump module and ‘ab’ to save to binary. As you can see, this works just the same way it would if this was outside a function. In this example, we are saving a lists and all the items in that lists are saved with the pickle module:  
```

class Processing:
   """ Process Data """
   @staticmethod
   def save_items_file(table, file):
       ''' Save data to file


       :param table: Inventory Table from main
       :param file: Inventory File from main
       :return: Nothing
       '''
       print('Would you like to save data')  # user input
       string = (str(input("Save 'y' or 'n'?: ")))  # creates new string from user input
       if string == 'y':  # if true executes below
           import pickle
           file = open(file, 'ab')  # open text file
           pickle.dump(table, file)
           file.close()  # closes file
           print('Data saved!')  # prints to user
       else:  # if false prints to user and ends program
           print('Data not saved!')
```
Figure 5 - Pickle Save to File  in Function 

## Unpickle in a function 
In just the same way, in figure 5, we can unpickle all the items in the list we created by using the pickle.load module. Once the data is extracted from the binary file can easily print out the data and do anything else with it.
```
@staticmethod
def see_data_in_file(file):
   '''  Shows data in file


   :return: nothing
   '''
   try:
       import pickle
       file = open(file, 'rb')  # open text file
       data = pickle.load(file)
       print('Here are the current items saved to file:')
       print('========================================')
       print('Item', 'Value', sep=' | ')
       for row in data:
           print(row[0], ' ' + row[1], sep=' | ')
       print('========================================')
       print()
   except:
       print('==============================================')
       print('File does not exist, try another option [1-4]')
       print('==============================================')
       print()
```
Figure 5 - Pickle Read from FIle in a Function

## Summary
This document demonstrated how pickling works to save objects into binary files and back. It is important to understand that while pickling is a way to compress data that is faster to process, it is an inherently insecure way of doing this. Programmers should know that this data is not encrypted and when unpickling, it is very important to do this with a trusted binary file to protect against malicious code being executed in your program.


## Running in PC 

![Screenshot 2023-03-05 at 4 23 04 PM](https://user-images.githubusercontent.com/125417260/222994822-bee0c536-ecd9-494e-8164-fc97add96691.png)  

Figure 6  - Running in PC


## Running in Terminal

![Screenshot 2023-03-05 at 4 23 11 PM](https://user-images.githubusercontent.com/125417260/222994840-e07d5d82-b584-4d81-aecc-6595d833722d.png)  

Figure 7 - Running in Terminal



## Pickle Sources

* [https://docs.python.org/3/library/pickle.html#data-stream-format](https://docs.python.org/3/library/pickle.html#data-stream-format)
* [https://pythonbasics.org/pickle/](https://pythonbasics.org/pickle/)
* [https://codefather.tech/blog/python-pickle/](https://codefather.tech/blog/python-pickle/)
* [https://pythonprogramming.net/python-pickle-module-save-objects-serialization/](https://pythonprogramming.net/python-pickle-module-save-objects-serialization/)
* [https://stackoverflow.com/questions/18963949/error-pickling-in-python-io-unsupportedoperation-read](https://stackoverflow.com/questions/18963949/error-pickling-in-python-io-unsupportedoperation-read)
* [https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)
* [https://www.synopsys.com/blogs/software-security/python-pickling/#:~:text=Pickle%20in%20Python%20is%20primarily,transport%20data%20over%20the%20network](https://www.synopsys.com/blogs/software-security/python-pickling/#:~:text=Pickle%20in%20Python%20is%20primarily,transport%20data%20over%20the%20network).

# Exception Handling in Python 
In Python, handling errors is done with the use of the Try-Except block. This is an important mechanism that puts guardrails around your program to prevent it from crashing or having unintended consequences when a human provides wrongful inputs. When building programs, take the time to think of and implement all potential scenarios in which a program might not function or could crash the program. 

There are several topics covered in this document related to error handling, these include: (a) Exceptions; (b) Handling Errors with Built-In Exceptions and (b) User-defined exceptions

## Exceptions 
In Python, there are Built-In Exceptions that are raised when the execution of a program is disrupted due to some type of error in the logic of  the program. In the example in figure 2, FileNotFoundError exception is raised when the file ‘MyData.txt’  cannot be found. When this happens the program simply terminates and stops working. 

```
# ------------------------------------------------- #
# Title: Error Handling Example 01 (Built-In)
# Description: A simple example of error handling
# ChangeLog: (Who, When, What)
# MValencia,2.26.2022,Created Script
# ------------------------------------------------- #


# Declare my variables
lstRow = []
strFile = None
objFile = None




# Process the data
strFile = input("Enter file name: ")
objFile = open(strFile, "r")
print(objFile)
objFile.close()


# Presentation
print(objFile)
```
Figure 1 -  Opening File  
![Screenshot 2023-03-05 at 4 26 17 PM](https://user-images.githubusercontent.com/125417260/222994952-3876ce9e-83a7-4b95-becc-fc29754fbcf7.png)    
Figure 2 - Exception FileNotFoundError  

## Handling Errors with Built-In Exceptions 
System errors that are generated by Python are oftentimes difficult for a human to understand. In Python, the Try-Except block is a way for a programmer to pass more user-friendly messages to help a user recover from an error. In the example below, in figure 3, by using the except clause and the FileNotFoundError exception, a more user-friendly message is passed to help recover from an error. There are many other Exception classes pre-built in Python that handle many types of errors, most of these are defined under the Exception class, such as the ArithmeticError for calculations errors, OSError for I/O errors or SyntaxError, when invalid syntax is used, that a programmer can include these in their code with Try-Except to anticipate all the different ways things can go wrong. 
```
# ------------------------------------------------- #
# Title: Error Handling Example 01 (Built-In)
# Description: A simple example of error handling
# ChangeLog: (Who, When, What)
# MValencia,2.26.2022,Created Script
# ------------------------------------------------- #


# Declare my variables
lstRow = []
strFile = None
objFile = None


# Process the data
strFile = input("Enter file name: ")
try:
   objFile = open(strFile, "r")
   print(objFile)
   objFile.close()
except FileNotFoundError:
   print("File does not exist in directory\n"
         "\tPlease provide the path or create a new file called,", strFile, "...try again")


# Presentation
print(objFile)
```
Figure 3 - Built in Exceptions  

![Screenshot 2023-03-05 at 4 26 49 PM](https://user-images.githubusercontent.com/125417260/222994979-cfaa8688-c620-4170-bb43-bedd3543be3b.png)   
figure 4 - User Friendly Exception Error  



## User-defined exceptions
User-defined exceptions in Python are created by programmers, see Figure 5. These are not built-in to the Python Exception class and are a useful way to place constraints on the input values that we want a program to accept. Examples are when we are looking for a specific range of numbers from a user, only wanting integers or strings as inputs or some other specific input to ensure the program works as expected.

In this example in Figure 5, we define AgeInvalidError under the Exception class if for example we don’t want an user to enter a value that is less than 0 - we can put these parameters in and when a user enters a negative number a message is printed asking for a valid value:
```
# Processing  ------------------------------------------------------------ #
class AgeInvalidError(Exception):
   """  Age or year value must be valid """
   def __str__(self):
       return 'Invalid correct age range or year'


class Processor:
   """  Performs Processing tasks """


   @staticmethod
   def calculate_year_born(age):
       '''  Calculates the year someone is born


       :param age:
       :return: none
       '''
       try:
           from datetime import date  # importing date class from datetime module
           todays_date = date.today()  # creating the date object of today's date
           if age <= 0:
               raise AgeInvalidError()
           year_born = todays_date.year - age
           print("The person was born in", year_born)
           print("=================================")
           print()
       except AgeInvalidError:
           print("Enter the correct age.")
```
Figure 5 - User Defined Exception  
![Screenshot 2023-03-05 at 4 27 16 PM](https://user-images.githubusercontent.com/125417260/222995030-46b35727-acf0-4787-b967-3875dac9cb83.png)  
Figure 6 - Incorrect Age Value  

## Running in PC  

![Screenshot 2023-03-05 at 4 31 47 PM](https://user-images.githubusercontent.com/125417260/222995306-631f50cf-aad8-4c41-b121-7756f951b203.png)  
Figure 7 - Running in PC  

## Running in Terminal  

![Screenshot 2023-03-05 at 4 28 10 PM](https://user-images.githubusercontent.com/125417260/222995131-b4bb9bfb-42b6-4192-80d2-e8156fbd78d0.png)  
Figure 8 - Running in Terminal  

## Learning Sites
I picked the following learning sites on the web because I found the information useful in how exception handling was defined and examples provided. The built-exceptions page in Python.org website does a good job going through the built-in exceptions and the logic of how they are organized. The two videos demonstrate easy examples around error handling. 

[Tutorialspoint - Exception Handling](https://www.tutorialspoint.com/python/python_exceptions.htm)

[Learning Python - Exception Handling](https://www.learnpython.org/en/Exception_Handling)

[Learning Python - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html#)

[Python.org - Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#Exception)

<h4>Videos</h4>


[Python Programming Tutorial - 28 - You are the only Exception](https://www.youtube.com/watch?v=1cCU0owdiR4&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=29)

[Python Tutorial: Using Try/Except Blocks for Error Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=20)




