import os
import shutil

# Define the file extensions for different categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Programs': ['.exe', '.msi', '.bat', '.sh'],
    'Others': []  # Files that don't match any category
}

# Function to organize files
def organize_files(directory):
    # Iterate over all files in the given directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Find the category for the file
        category_found = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                move_file_to_category(directory, filename, category)
                category_found = True
                break

        # If no category was found, move it to 'Others'
        if not category_found:
            move_file_to_category(directory, filename, 'Others')

# Function to move a file to its categorized folder
def move_file_to_category(directory, filename, category):
    # Create the category folder if it doesn't exist
    category_path = os.path.join(directory, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

    # Move the file to the category folder
    shutil.move(os.path.join(directory, filename), os.path.join(category_path, filename))
    print(f'Moved: {filename} --> {category}/')

# Main function
if __name__ == "__main__":
    # Input the directory to organize
    directory = input("Enter the path to the directory you want to organize: ").strip()

    if os.path.exists(directory) and os.path.isdir(directory):
        organize_files(directory)
        print("File organization completed!")
    else:
        print("Invalid directory path. Please enter a valid directory.")
