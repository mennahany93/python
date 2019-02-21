#! /usr/bin/python3
import sys
from classes import *

def menu():
    print("**************MAIN MENU****************")
    choice = input("""
                      1: Create Database
                      2: Insert Data
                      3: Search
                      4: Drop Database or table
                      5: Print all databases
                      6: Quit

                      Please enter your choice: """)

    if choice == "1":
        create_database()
    elif choice =="2":
        insert_data()
    elif choice == "3":
        search()
    elif choice =="4":
        drop_database()
    elif choice =="5":
        print_databases()
    elif choice == "6":
        sys.exit(0)
    else:
        print ("Wrong entry ,please choose a number from menu")


def create_database():
    name=input("Enter name of database: ")
    d=database(name)
    d.add_to_list
    print(list_of_databases)


def print_databases():
    print (list_of_databases)




while True:
    menu()
