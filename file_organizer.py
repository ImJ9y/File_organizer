import os
import shutil
from pathlib import Path

# Define file extensions and their corresponding directories
file_extensions = {
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'pdf': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'avi': 'Videos',
    'fiv': 'Videos',
    'wmv': 'Videos'
}

def organize_files(directory):
    # Create the directory if it does not exist
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist. Creating it...")
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    # Create directories for each file type if they don't exist
    for extension, folder in file_extensions.items():
        folder_path = os.path.join(directory, folder)
        Path(folder_path).mkdir(parents=True, exist_ok=True)
    
    # Move files to their corresponding directories
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            if file_extension in file_extensions:
                target_folder = os.path.join(directory, file_extensions[file_extension])
                target_path = os.path.join(target_folder, filename)
                try:
                    shutil.move(file_path, target_path)
                    print(f"Moved: {filename} to {target_folder}")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    #Enter the folder that you would like to organize the files
    organize_files("/Users/j9yim/Desktop/Coding/file_organizer")
