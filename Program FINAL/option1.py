#imports all the neccessary modules
import pandas as pd
import re
from colors import fgColorsByAni as fg
from colors import bgColorsByAni as bg
from colors import stylesByAni as s


# login through Id
def login(df): 
    # loop until the user enters a valid input
    while True: 
        print(s.r +
              "----------------"*4 + s.i)
        inp = input(fg.brightBlue + s.b + s.i
                     # ask for the user's input
                    + "Please input your ID number or enter to exit: "
                    + s.r + " ")
         # check if the input is in the correct format (2 capitalised letters followed by 2 numbers)
        if re.match("(^[A-Z]{2}[0-9]{2}$)", inp):  
            # check if the input is in the database
            match = False
            for i in df.index:
                # get the id from the database
                id = df.loc[i, "id"]
                # check if the input is in the database
                if inp == id:
                    # get the name from the database that corresponds to the id
                    name = df.loc[i, "name"]
                    print(s.r + "----------------"*4)
                    #Welcomes the user
                    print(fg.pg + s.b + s.u + f"Welcome,{name}"
                          + s.r)
                    # get the number of properties from the database
                    prop = df.loc[i, "number_of_props"]
                    round(prop, 0)
                    #Displays properties sold
                    print(f"You have sold {int(prop)} properties")
                    #Give them the option to repeat the login
                    print("Do you want to enter another ID?")
                    option = input(fg.md + bg.white + s.b + s.i
                                   + "Enter to exit or press any \
key than enter to continue: " + s.r)
                    print()
                    match = True
                    # if the user enters nothing, exit the program
                    if option == "":
                        return

            # if the input is not in the database, display an error message and returns to Id request
            if not match:
                print(fg.red + "Invalid ID" + s.r)
        elif inp == "":
            return
         #check if the input is in the correct format (2 capitalised letters followed by 2 numbers)
        elif not re.match("(^[A-Z]{2}[0-9]{2}$)", inp):
            print(fg.red + "Invalid input,please try again" + s.r)

# sign up through name
def sign_name(df):
    # loop until the user enters a valid input
    while True:
        print(s.r + "----------------"*4)
        # ask for the user's input
        name = input(fg.brightBlue + s.i + s.b +
                     "Please input your name:" + s.r + " ")
        # check if the input is in the correct format (only letters and the length is between 2 and 12) 
        if name.isalpha():
            if 1 < len(name) <= 12:
                print(fg.pg + "Thank you, name is accepted" + s.r)
                print(s.r + "----------------" * 4)
                # if all the correct conditions have been met it will call the sign_id_and_props function
                df = sign_id_and_props(name, df)
                return df
            # if the input is not in the correct format, display an error message and returns to name request
            print(fg.red + "Invalid name length,please try again"
                  + s.r + "\n" + bg.py + fg.md + s.i + s.b
                  + "(The length should be 2 to 12 characters)" + s.r)
        # if the input is not in the correct format, display an error message and returns to name request
        elif not name.isalpha():
            print(bg.py + fg.md + s.i + s.b
                  + "- Use letters only!" + s.r)
        else:
            print("Unknown error,please try again")

#sign up through Id and properties sold
def sign_id_and_props(name, df):
    # loop until the user enters a valid input
    while True:
        # ask for the user to create an ID number
        ids = input(fg.brightBlue + s.b + s.i
                    + "Please input your Desired ID number" + s.r + "\n"
                    + bg.py + fg.md + s.i + s.b
                    + "(must be 2 capitalised letters followed by 2 numbers)"
                    + s.r + "\n"
                    + fg.brightBlue + s.b + s.i
                    + "Input:" + s.r + " ")
         #check if the input is in the correct format (2 capitalised letters followed by 2 numbers)
        if re.match("(^[A-Z]{2}[0-9]{2}$)", ids):
            match = False
            for x in df.index:
                # check if the ID is already in the database
                if df.loc[x, "id"] == ids:
                    print(fg.red +
                          "ID was taken, please try again"
                          + s.r)
                    match = True
                elif not re.match("(^[A-Z]{2}[0-9]{2}$)", ids):
                    print(fg.red +
                          "Invalid input,please try again"
                          + s.r)
            # if the ID is not already in the database , it will ask for the number of properties sold
            if not match:
                valid = True
                while valid:
                    try:
                        # ask for the user to input the number of properties sold
                        prop = int(input(fg.brightBlue + s.b + s.i +
                                         "Please enter the amount \
of properties sold: " + s.r))
                        valid = False
                    #Makes sure input is a number
                    except ValueError:
                        print(fg.red +
                              "Invalid input,please use numbers only"
                              + s.r)
                        valid = True
                    #Makes sure the properties sold is between 0 and 150
                    if 0 <= prop <= 150:
                        # add the name, id and number of properties sold to the database
                        length = len(df.index)
                        df.loc[length, "name"] = str(name)
                        df.loc[length, "id"] = ids
                        df.loc[length, "number_of_props"] = prop
                        print(fg.pg + s.b +
                              "Thank you for signing up!" + s.r)
                        return df
                    else:
                        print(fg.red +
                              "Invalid property number,please try again" + s.r)
        else:
            print(fg.red +
                  "Invalid ID,please try again" + s.r)


#login or sign main menu
def log_or_sign(df):
    menu = fg.brightBlue + s.b \
           + "Welcome to the details input " + s.r

    menu += "\nWhat would you like to do?: "
    #Login option
    menu += fg.brightBlue
    menu += " \n["
    menu += s.r
    menu += "1"
    menu += fg.brightBlue
    menu += "]"
    menu += s.r
    menu += " - Login"
    #Signup option
    menu += fg.brightBlue
    menu += " \n["
    menu += s.r
    menu += "2"
    menu += fg.brightBlue
    menu += "]"
    menu += s.r
    menu += " - Signup"
    #Exit option
    menu += fg.brightBlue
    menu += " \n["
    menu += s.r
    menu += "3"
    menu += fg.brightBlue
    menu += "]"
    menu += s.r
    menu += " - Exit"
    # loop until the user enters a valid input
    while True:
        print(fg.brightBlue + "----------------"*4
              + s.r)
        # display the menu
        print(menu)
        print(fg.brightBlue + "----------------" * 4
              + s.r)
        user_choice = input(
            bg.white + fg.md + s.b + s.i +
            "Please select the number next to the option you will pick:"
            + s.r + " ")
        #all options
        if user_choice == "1":
            login(df)
        elif user_choice == "2":
            df = sign_name(df)
        #if they want to exit,sends to main menu
        elif user_choice == "3":
            return df
        else:
            print(fg.red +
                  "Invalid input, please try again"
                  + s.r)


if __name__ == "__main__":
    # opens the csv file
    df = pd.read_csv("data.csv")
    log_or_sign(df)
