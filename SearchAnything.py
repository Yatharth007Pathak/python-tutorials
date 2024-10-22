# Search anything in python

import pywhatkit as kit
searchitem=(input("Enter the topic: "))
try:
    kit.info(searchitem, 20)
except Exception as e:
    print(f"An error occurred: {e}")


'''
Here's a breakdown of the provided code, which uses the pywhatkit library to search for information on a specific topic:

import pywhatkit as kit
Importing pywhatkit: This imports the pywhatkit library and gives it the alias kit. 
pywhatkit is a library that can be used for various tasks like sending WhatsApp messages, searching for information, 
playing YouTube videos, and more.

searchitem = (input("Enter the topic: "))
Getting User Input: This line prompts the user to enter a search topic. The input is stored in the variable searchitem.

try:
    kit.info(searchitem, 20)
Using kit.info(): The kit.info() function searches for information on the provided topic.
searchitem: This is the topic the user entered, which will be searched.
20: This specifies the number of lines to display from the search result. 
In this case, it will display up to 20 lines of information related to the search item.

except Exception as e:
    print(f"An error occurred: {e}")
Exception Handling: If any error occurs during the execution of the kit.info() function (such as an invalid search or connection error), 
it will be caught by this except block. The error message will be printed in the format: "An error occurred: [error message]".


Possible Error Scenarios
Network Error: If there's no internet connection, an exception will be thrown, and the message will indicate a connection issue.
Invalid Input: If the input provided cannot be searched or causes an error in the library, the exception message will reflect that.
'''