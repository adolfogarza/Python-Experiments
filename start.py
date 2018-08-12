'''
    File name: start.py
    Author: Adolfo Garza
    Date created: 08/11/2018
    Date last modified: 08/11/2018
    Python Version: 3.6

    Description: Entry point of the script, presents title and launches main
    requestable launch sequence.
'''
from graduate import Graduate


def main():
    print("\n--------------------------------")
    print("Request Bot: Fetch Graduate Data")
    print("Coder: Adolfo Garza")
    print("Last updated: August, 11, 2018")
    print("--------------------------------\n")

    Graduate().launch_sequence()


if __name__ == "__main__":
    main()
