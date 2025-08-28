import os

def modify_and_save_file():
    """
    Prompts the user for a filename, reads its content,
    converts the text to uppercase, and saves it to a new file.

    Includes error handling for missing files.
    """
#  Asking the user for the input filename
    input_filename = input("Enter the name of the file to read: ")
    output_filename = "modified_output.txt"

    try:
        #  Opening the file and reading its contents
