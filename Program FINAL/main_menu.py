# IMPORTING PACKEGES
import time
import pandas as pd
from option1 import log_or_sign
from option2 import data
from option34 import delete, save
from option34 import delete, save
from colors import fgColorsByAni as fg
from colors import bgColorsByAni as bg
from colors import stylesByAni as s


# main manu function will display options
def main_menu():
    """
    This function will display main menu options,
    ask user for input and refer user to the next required function
    """
    # it will try to read csv,
    # if error occurs it will automatically create new csv
    try:
        # read csv
        df = pd.read_csv("Data.csv")
    except ValueError:
        # create csv
        df = pd.DataFrame({'name': [], 'id': [], 'number_of_props': [],
                           'pay(£)': [], 'pay_with_bonus(£)': []})

    print(fg.mg + r"""
                            ____    __    ____  _______  __        ______   ______   .___  ___.  _______
                            \   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
                             \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__
                              \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|
                               \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____
                                \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|
    """ )
    time.sleep(0.6)
    print(r"""
                                                     ______   ______
                                                    /\__  _\ /\  __ \
                                                    \/_/\ \/ \ \ \/\ \
                                                       \ \_\  \ \_____\
                                                        \/_/   \/_____/
       """)
    time.sleep(0.6)
    print(r"""
                                    ____  _____    _    ____    ____      _    ___ _   _ ____ 
                                    |  _ \| ____|  / \  |  _ \  |  _ \    / \  |_ _| \ | / ___|
                                    | |_) |  _|   / _ \ | | | | | |_) |  / _ \  | ||  \| \___ \
                                    |  _ <| |___ / ___ \| |_| | |  _ <  / ___ \ | || |\  |___) |
                                    |_| \_\_____/_/   \_\____/  |_| \_\/_/   \_\___|_| \_|____/
       """ + s.r)
    time.sleep(0.6)
    print(fg.fp + r"""
                                        ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔═╗╔╦╗╔╗ ╔═╗╦═╗╔═╗  ╔═╗╔╗╔╦ ╦ ╦
                                        ╚═╗ ║ ╠═╣╠╣ ╠╣   ║║║║╣ ║║║╠╩╗║╣ ╠╦╝╚═╗  ║ ║║║║║ ╚╦╝
                                        ╚═╝ ╩ ╩ ╩╚  ╚    ╩ ╩╚═╝╩ ╩╚═╝╚═╝╩╚═╚═╝  ╚═╝╝╚╝╩═╝╩
           """ + s.r)

    time.sleep(0.6)

    # This is a while loop that will display main menu
    # and usk user to choose one option to move on
    while True:
        print(fg.lilac +
              "*" * 21 + "Welcome to main menu" + "*" * 21
              + s.r)
        print(fg.lilac + "[" + s.r + "1" +
              fg.lilac + "]" + s.r, "Data input")
        print(fg.lilac + "[" + s.r + "2" +
              fg.lilac + "]" + s.r, "Data Reading")
        print(fg.lilac + "[" + s.r + "3" +
              fg.lilac + "]" + s.r, "Save to CSV")
        print(fg.lilac + "[" + s.r + "4" +
              fg.lilac + "]" + s.r, "Delete the CSV")
        print(fg.lilac + "[" + s.r + "5" +
              fg.lilac + "]" + s.r, "Exit" + s.r)

        # user input
        option = input(bg.py + fg.dcp + s.i + s.b
                       + "Please choose one option from the list,"
                       + s.u + "ex. 2:"
                       + s.r + " ")

        # This is an if statement that will call right function
        # depending on a user's choice
        if option == "1":
            df = log_or_sign(df)
        elif option == "2":
            df = data(df)
        elif option == "3":
            save(df)
        elif option == "4":
            delete()
        elif option == "5":
            print(fg.lilac + s.invert
                  + "THANK YOU FOR USING OUR PROGRAM" + s.r)
            print(fg.red + "Exiting..." + s.r)
            break
        else:
            print(fg.red + s.i + "Invalid input, please try again" + s.r)


main_menu()
