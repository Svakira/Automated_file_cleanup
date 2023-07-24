import os
import re

def clean_text(text, regex_list):
    # Remove leading and trailing whitespaces from the text
    cleaned_text = text.strip()
    
    # Remove specified regular expressions from the regex_list
    for regex_pattern in regex_list:
        cleaned_text = re.sub(regex_pattern, '', cleaned_text)
    
    return cleaned_text

def clone_and_clean_files(folder_path, regex_list):
    # Check if the folder path is valid
    if not os.path.exists(folder_path):
        print("Invalid folder path.")
        return
    
    # Create a new folder with the suffix "_cleaned"
    new_folder_path = folder_path + "_cleaned"
    os.makedirs(new_folder_path, exist_ok=True)
    
    # Get the list of files in the folder
    file_list = os.listdir(folder_path)
    
    for file_name in file_list:
        # Check if the element is a file (not a directory)
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            # Read the content of the file
            with open(file_path, 'r', encoding='latin-1') as file:
                text = file.read()
            
            # Clean the text using the clean_text function
            cleaned_text = clean_text(text, regex_list)
            
            # Create the new file with the suffix "_cleaned"
            new_file_name = os.path.splitext(file_name)[0] + "_cleaned" + os.path.splitext(file_name)[1]
            new_file_path = os.path.join(new_folder_path, new_file_name)
            
            # Write the clean text into the new file
            with open(new_file_path, 'w', encoding='latin-1') as new_file:
                new_file.write(cleaned_text)

if __name__ == "__main__":
    # Ask the user for the folder path and regular expressions
    folder_path = input("Enter the folder path: ")
    regex_list = input("Enter the regular expressions separated by commas: ").split(',')
    
    # Call the function to clone and clean the files
    clone_and_clean_files(folder_path, regex_list)
    print("Process completed.")
