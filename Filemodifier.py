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
with open(input_filename, 'r') as file:
            original_content = file.read()
            print(f"\nSuccessfully read content from '{input_filename}'.")
            print("-" * 30)
            print("Original content:")
            print(original_content)
            print("-" * 30)

        # Modify the content (convert to uppercase)
        modified_content = original_content.upper()

        #  Write the modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
