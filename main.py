# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from  getTabProps import getTabProperties
from sqlCreateTables import createTable
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    n, l = getTabProperties(r"C:\diskd\a16.csv")
    print(n)
    print(l)
    createTable (n,l)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
