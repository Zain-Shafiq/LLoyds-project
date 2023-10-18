# IMPORTING PACKAGES
import pandas as pd6
from time import sleep
from colors import fgColorsByAni as fg
from colors import bgColorsByAni as bg
from colors import stylesByAni as s


def delete():
    while True:
        # options menu
        print(fg.red + "----------------"*4 +
              "\nThis section is for deleting your data")
        print(fg.red + "["
              + s.r + "1"
              + fg.red + "]"
              + s.r + "- delete")
        print(fg.red + "["
              + s.r + "2"
              + fg.red + "]"
              + s.r + "- return to the main menu")

        # user input
        print("\n")
        option = input(bg.py + fg.dr + s.b + s.i
                       + "Please choose one option from above:"
                       + s.r + " ")

        # this will execute the code depending on the user's choice
        if option == "1":

            print("\n")
            confirmation = input(
                fg.red + "Confirmation!"
                + s.r + "\n"
                + bg.py + fg.dr + s.b + s.i
                + "Please press Y / N:" + s.r + " ").lower()

            if confirmation == "y":
                f = open("Data.csv", "w")
                f.truncate()
                f.close()
                print(s.b + "*DELETED*" + s.r)
                print(s.i +
                      "Returning to the main menu in ..."
                      + s.r)
                x = 0
                y = 0
                while x >= 0:
                    x += 1
                    y += 1
                    print(fg.red + str(y) + s.r)
                    if x == 3:
                        break
                    sleep(0.5)
                return

            elif confirmation == "n":
                pass
            else:
                print(
                    fg.red +
                    "Invalid input"
                    + fg.red)
                print(bg.py + fg.dr + s.b + s.i
                      + " Note! your answer should be Y/y or N/n!"
                      + s.r)

        elif option == "2":
            return
        else:
            print(
                fg.red +
                "Invalid input"
                + fg.red)
            print(bg.py + fg.dr + s.b + s.i
                  + " Note! your answer should be 1 or 2"
                  + s.r)


def save(df):
    while True:
        # options menu
        print(
            fg.green + "----------------"*4
            + "\nThis section is for saving your data" + fg.green)
        print(fg.green + "["
              + s.r + "1"
              + fg.green + "]"
              + s.r + "- save")
        print(fg.green + "["
              + s.r + "2"
              + fg.green + "]"
              + s.r + "- return to the main menu")

        # user input
        print("\n")
        option = input(bg.py + fg.pg + s.b + s.i
                       + "Please choose one option from above:"
                       + s.r + " ")

        # this will execute the code depending on the user's choice
        if option == "1":
            print("\n")
            confirmation = input(fg.green + "Confirmation!"
                                 + s.r + "\n"
                                 + bg.py + fg.pg + s.b + s.i
                                 + "Please press Y / N:" + s.r + " ").lower()

            if confirmation == "Y" or confirmation == "y":
                print("saving test...")
                df.to_csv("data.csv", index=False)
                break

            elif confirmation == "N" or confirmation == "n":
                df.to_csv("data.csv", index=False)
                print(s.b + "*SAVED*" + s.r)
                print(s.i +
                      "Returning to the main menu in ..."
                      + s.r)
                x = 0
                y = 0
                while x >= 0:
                    x += 1
                    y += 1
                    print(fg.pg + str(y) + s.r)
                    if x == 3:
                        break
                    sleep(0.5)
                return

            else:
                print(
                    fg.red +
                    "Invalid input"
                    + fg.red)
                print(bg.py + fg.pg + s.b + s.i
                      + " Note! your answer should be Y/y or N/n!"
                      + s.r)

        elif option == "2":
            break

        else:
            print(fg.red +
                  "Invalid input")
            print(bg.py + fg.pg + s.b + s.i
                  + " Note! your answer should be 1 or 2!"
                  + s.r)
