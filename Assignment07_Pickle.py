#-----------------------------------------------------#
# Title: Home Inventory Script
# Dev: MValencia
# Desc: Demonstrate how two store and
# add data to a two dimensional table
# Data: Feb 6, 2023
# Changelog: (Who, When, What)
#   MValencia, 2/6/2023, created script
#-----------------------------------------------------#

# Data ------------------------------------------------------------------  #
list_table = [] # empty list table
menu_option = ''
file_Obj = 'HomeInventory.pickle'


# Processing  ------------------------------------------------------------ #
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

# Presentation (Input/Output)  ------------------------------------------- #

class IO:
    """ Performs Input and Output tasks """
    @staticmethod
    def input_menu_options():
        ''' Display a menu of choices to the user

             :return: nothing
                '''
        print('''Track Home Inventory:
            1) Add Data to the List,
            2) Display Current Data,
            3) See Data in File
            4) Exit and Save to File''')

    @staticmethod
    def input_menu_choice():

        '''  Menu choice is displayed

            :return: menu choice
                '''
        choice = input('Select Menu Options [1 to 3]: ')  # user input
        print()  #  friendly line
        return choice

    @staticmethod
    def input_task_items(table):
        ''' Collects user inputs

        :param table: list containing user data
        :return: returns list of user data
        '''

        item = str(input("Enter Item: "))  # user input stored
        value = str(input("Enter value: "))  # user input stored
        row = [item.strip(), value.strip()]  # user inputs stored in a row
        table.append(row)   # user input stored in a table
        return table

    @staticmethod
    def print_tasks_table(table):
        '''  Prints content of user data

        :param table: inputs content of user data
        :return: nothing
        '''
        print("Current Items on your list:")  # print to user
        print('========================================')
        print(' ', 'Item', 'Value', sep= ' | ')
        for row in table:  # looks for rows in the table
            print(' ', row[0], ' ' + row[1], sep=' | ')  # prints rows from the table
        print('========================================')


 # Main Body of Script  -------------------------------------------------- _#


while(True):
    # Step 1  Display a menu of choices to the user
    IO.input_menu_options()
    menu_option = IO.input_menu_choice()

    # Step 2
    # Add a new item to the List(Table) each time the user makes that choice
    if menu_option == '1': # first choice
        list_table = IO.input_task_items(list_table)
        continue

    # Step 3
    # Display the data in the List(Table) each time the user makes that choice
    elif menu_option == '2':  # second choice
        IO.print_tasks_table(table = list_table)
        continue

    # Step 4
    # Read data from file
    elif menu_option == '3':  #  third choice
        Processing.see_data_in_file(file_Obj)

    #step 5
    # Exit the program and save the data to a text file when the user makes that choice
    elif menu_option == '4': #third choice
        Processing.save_items_file(table = list_table, file = file_Obj)
        break

