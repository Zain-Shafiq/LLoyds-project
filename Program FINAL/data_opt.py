"""
This is the function page for the options in option2.py
"""
import pandas as pd
from colors import fgColorsByAni as fg
from colors import bgColorsByAni as bg
from colors import stylesByAni as s


def overall(df0):
    """
    This function is to display the ranking of the employees
    in order of the number of properties sold.
    """
    # Sort the values decending by the number of properties sold
    ova = df0.sort_values(
        by=["number_of_props"], ascending=False, inplace=False
    ).reset_index(drop=True)
    # Drop any data that is irrevelent
    ova.drop(["pay(£)", "pay_with_bonus(£)"], axis=1, inplace=True)
    # display the data properply
    print(fg.lcp + "----------------" * 4)
    print("The Ranking in order of the number of properties sold: " + s.r)
    print(ova)
    print(fg.lcp + "----------------" * 4 + s.r)
    # gives time for the user to read until they press enter
    input(fg.green + "Press enter to exit   " + s.r)


def sales(df0, real):
    """
    This addes the pay amount to the table
    """
    # Calculate the pay amount
    for lines in df0.index:
        temp = df0.loc[lines, "number_of_props"] * 500
        # round off the data to 2 decimal places
        df0.loc[lines, "pay(£)"] = round(temp, 2)
    # The "if real" is used to check is this a backend process or not,
    # True for front end (display the data)
    # False for back end (do NOT display the data)
    if real:
        # Sort the values again
        sal = df0.sort_values(
            by=["number_of_props"], ascending=False, inplace=False
        ).reset_index(drop=True)
        # drop the unnecessart columns
        sal.drop(["pay_with_bonus(£)"], axis=1, inplace=True)
        # display the data gracefully
        print(fg.lcp + "----------------" * 4)
        print("The sales commission paid to each employee: " + s.r)
        print(sal)
        print(fg.lcp + "----------------" * 4)
        input(fg.green + "Press enter to exit   " + s.r)
    # Return the modified dataframe
    return df0


def bonus(df0, real):
    """
    This function calculates who is going to get the bonus and
    how much will he/she get
    """
    # Check whether the pay has been calculated or not
    # If not, do function "sales" in backend
    if df0["pay(£)"].isnull().values.any():
        df0 = sales(df0, False)  # False for backend
    # sort the dataframe accoring to the number of properties
    df0.sort_values(by=["number_of_props"], ascending=False, inplace=True)
    df0.reset_index(drop=True, inplace=True)
    for row in df0.index:
        # assign the 15% bonus to the person that has the most properties sold
        if row == 0:
            temp = df0.loc[row, "pay(£)"] * 1.15
            df0.loc[row, "pay_with_bonus(£)"] = round(temp, 2)
        elif row != 0:
            df0.loc[row, "pay_with_bonus(£)"] = df0.loc[row, "pay(£)"]
    # The "if real" is used to check is this a backend process or not,
    # True for front end (display the data)
    # False for back end (do NOT display the data)
    if real:
        # display the data gracefully
        print(fg.lcp + "----------------" * 4)
        print("The Table with bonus commision: " + s.r)
        print(df0)
        print(fg.lcp + "----------------" * 4 + s.r)
        input(fg.green + "Press enter to exit   " + s.r)
    return df0


def prop(df0):
    """
    This function is use to calculate and show
    the total number of properties sold by the company
    """
    # Setting the initial count
    count = 0
    # adding the counts
    for rows in df0.index:
        count += df0.loc[rows, "number_of_props"]
    # display the data gracefully
    print(fg.lcp + "----------------" * 4 + s.r)
    print(f"The total number of properties sold by the company is: {count}")
    print(fg.lcp + "----------------" * 4 + s.r)
    input(fg.green + "Press enter to exit   " + s.r)


def comm(df0):
    """
    This function is used to calculate and show
    the total commission the company needed to pay
    """
    # Check whether the "pay with bonues has been generated"
    # if yes, ignore it
    # if no, Run "bonus" in the back end
    if df0["pay_with_bonus(£)"].isnull().values.any():
        df0 = bonus(df0, False)  # False for backend
    amo = 0  # Set the initial count
    # adding the counts
    for row in df0.index:
        amo += df0.loc[row, "pay_with_bonus(£)"]
    # display the data gracefully
    print(fg.lcp + "----------------" * 4 + s.r)
    print(f"The total commission the company needed to pay is: {amo}")
    print(fg.lcp + "----------------" * 4 + s.r)
    input(fg.green + "Press enter to exit   " + s.r)


def all1(df0):
    """
    This displays the whole table.
    """
    # display the data gracefully
    print(fg.lcp + "----------------" * 4)
    print("The whole table: " + s.r)
    print(df0)
    print(fg.lcp + "----------------" * 4 + s.r)
    input(fg.green + "Press enter to exit   " + s.r)


# just for testing purposes
if __name__ == "__main__":
    dfn = pd.read_csv("data.csv")
    dfn = bonus(dfn, True)
