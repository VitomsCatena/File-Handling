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

print(f"Content has been modified and saved to '{output_filename}'.")
        print("\nModified content:")
        print("-" * 30)
        print(modified_content)
        print("-" * 30)

except FileNotFoundError:
        # specific error handling if the file doesn't exist
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please make sure the file exists in the correct directory.")
    except Exception as e:
        # 6. Handling any other potential errors
        print(f"\nAn unexpected error occurred: {e}")

# Calling the main function to run the program
if __name__ == "__main__":
    # Creating a dummy file for testing the success case
    if not os.path.exists("example.txt"):
        with open("example.txt", "w") as f:
            f.write("This is a test file.\n")
            f.write("It contains multiple lines.")
    
    # Running the program
    modify_and_save_file()
