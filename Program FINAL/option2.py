"""option functions were imported"""
import pandas as pd
from data_opt import overall, sales, bonus, prop, comm, all1
from colors import fgColorsByAni as fg
from colors import bgColorsByAni as bg
from colors import stylesByAni as s


def data(df1):
    """This is the main menu for reading the data"""
    # read the CSV or input data frame from outside
    df0 = df1
    if df1 is None:
        try:
            df0 = pd.read_csv("data.csv")
        except FileNotFoundError:
            print("No data found")
            return

    while True:
        # menu
        print(fg.fp + "----------------"*4 + fg.lcp)
        print("Which data do you want to read?" + s.r)
        print(
            """[1] Ranking in order of the number of properties sold.
[2] Calculate the sale commission paid to each employees
[3] The bonus to the commission
[4] The total properties sold by the company
[5] The total commission the company
[6] Show the whole table
[7] Exit this segment"""
        )
        # get the option and direct to the specific function
        print(fg.fp + "----------------"*4)
        option = input(bg.white + fg.dcp + s.b + s.i
                       + "Please enter your option here:"
                       + s.r + " ")
        if option == "1":
            overall(df0)
        elif option == "2":
            df0 = sales(df0, True)
        elif option == "3":
            df0 = bonus(df0, True)
        elif option == "4":
            prop(df0)
        elif option == "5":
            comm(df0)
        elif option == "6":
            all1(df0)
        elif option == "7":
            return df0
        else:
            print("Invalid input, please try again")


if __name__ == "__main__":
    data(None)
