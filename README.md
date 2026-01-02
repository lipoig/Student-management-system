# Student Managament System

## Overview

The **Student Managament System** is a simple console-based Python
application that allows users to manage a list of people using a unique
personal code. The program supports adding, removing, searching, and
displaying persons through a menu-driven interface.

This project demonstrates basic Python concepts such as: -
Object-Oriented Programming (OOP) - Dictionaries for data storage - User
input handling - Menu-based program flow

------------------------------------------------------------------------

## Features

-   Add a person with first name, surname, and personal code
-   Prevent duplicate personal codes
-   Remove a person by personal code
-   Remove a person by first name and surname
-   Search for persons by first name
-   Display all stored persons
-   Simple text-based menu interface

------------------------------------------------------------------------

## Requirements

-   Python 3.x\
    (No external libraries required)

------------------------------------------------------------------------

## How to Run

1.  Save the Python code in a file, for example:

        person_storage.py

2.  Open a terminal or command prompt.

3.  Run the program using:

    ``` bash
    python person_storage.py
    ```

------------------------------------------------------------------------

## Menu Options

    1. Add person
    2. Remove person by personal code
    3. Remove person by first and last name
    4. Search by name (displays last person's surname)
    5. Display all persons
    6. Exit

### Description of Options

-   **Add person**\
    Adds a new person if the personal code does not already exist.

-   **Remove person by personal code**\
    Removes a person using their unique personal code.

-   **Remove person by first and last name**\
    Removes the first matching person found with the given name and
    surname.

-   **Search by name**\
    Finds all persons with the given first name and displays the surname
    of the last found match.

-   **Display all persons**\
    Prints all persons currently stored in the system.

-   **Exit**\
    Ends the program.

------------------------------------------------------------------------

## Example Output

    Name: John Doe, Personal Code: 12345
    Name: Jane Smith, Personal Code: 67890

------------------------------------------------------------------------

## Notes

-   All data is stored in memory and will be lost when the program
    exits.
-   Name comparisons are case-insensitive.
-   Only one person is removed when deleting by name.

------------------------------------------------------------------------

