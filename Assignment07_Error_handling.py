# ----------------------------------------------------------------------------#
# Title: The Age Verification Program
# Description: A program that tell you information about your birthday
# ChangeLog: (Who, When, What)
# MValencia,2.26.2022,Created Script
# -----------------------------------------------------------------------  #

# Data ------------------------------------------------------------------  #
choice_str = ""  # Capture user selection from menu
year_int = "" # Capture user input year born

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


    @staticmethod
    def calculate_age (year):
        '''  Calculates the age of someone

        :param year:
        :return: none
        '''
        try:
            from datetime import date  # importing date class from datetime module
            todays_date = date.today()  # creating the date object of today's date
            if year > todays_date.year:
                raise AgeInvalidError
            age = todays_date.year - year
            print("The person is", age, "years old")
            print('==================================')
        except:
            print("Enter a valid year")

# Presentation (Input/Output)  ------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def hello_message():
        '''  Prints a welcome message

        :return: nothing
        '''

        print('''
        =========================================================
        |  Welcome to the age verification tool. This is a user |
        |  friendly tool to help calculate the year someone     |
        |  was born or their age.                               |
        =========================================================
         ''')

    @staticmethod
    def input_menu_options():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Please select an option from the menu below [1-3]:
        1) Calculate Year Born
        2) Calculate Age 
        3) Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        '''  Menus choice is displayed

        :return: nothing
        '''
        choice = str(input("Choose a menu option [1-3]: "))
        print() #  friendly display line
        return choice

    @staticmethod
    def input_year_born():
        '''  Input request for year born

        :return: year
        '''
        year = int(input("Enter year born: "))
        print()  #  friendly display line
        return year

    @staticmethod
    def input_age ():
        '''  Input request for age

        :return: age
        '''
        try:
            age = int(input("Enter age: "))
            print() # friendly display line
            return age
        except AgeInvalidError:
            print("Enter a valid age")
# Main Body of Script  -------------------------------------------------- _#

IO.hello_message()
while (True):
    #  Step 1: when the program starts it displays a welcome message and menu choice
    IO.input_menu_options()
    choice_str = IO.input_menu_choice()

    #  Step 2: processes user's choice
    if choice_str.strip() == '1': #  show age
        age_int = IO.input_age()
        Processor.calculate_year_born(age_int)
        continue #  to show the menu

    elif choice_str.strip() == '2': #  show the year born
        year_int = IO.input_year_born()
        Processor.calculate_age(year_int)
        continue #  to show the menu

    elif choice_str.strip() == '3':
        print("Thank for use the age tool, goodbye!")
        break # end existing tool

