import os
import stat
import datetime

def is_safe_path(path):
    """Check if the given path is safe to access."""
    safe_characters = set("abcdefghijklmnopqrstuvwxyz0123456789._-/\:")
    return all(char in safe_characters for char in path.lower())

def depth_first_search(directory, target_filename):
    """Searches for a file using Depth-First Search and returns file details if found."""
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if not is_safe_path(item):
            continue
        if os.path.isfile(full_path):
            if item == target_filename:
                file_stats = os.stat(full_path)
                return {
                    'path': full_path,
                    'size': file_stats.st_size,  # Size in bytes
                    'created': file_stats.st_ctime,  # Creation time
                    'modified': file_stats.st_mtime  # Last modification time
                }
        elif os.path.isdir(full_path):
            result = depth_first_search(full_path, target_filename)
            if result:
                return result
    return None  # File not found

def main():
    """Prompts for filename, performs the search, and displays results."""
    # Implement user authentication and authorization mechanisms here
    filename = input("Enter the name of the file to find (including the file extension): ")

    # Input validation
    if not is_safe_path(filename):
        print("Error: Filename should contain only letters, numbers, and a valid file extension.")
        return

    start_directory = input("Enter the starting directory for the search: ")
    if not os.path.isdir(start_directory) or not is_safe_path(start_directory):
        print("Error: Invalid starting directory.")
        return

    result = depth_first_search(start_directory, filename)

    if result:
        print("File found!")
        print(f"Full Path: {result['path']}")
        print(f"File Size: {result['size'] / (1024 * 1024)} MB")
        print(f"Created: {datetime.datetime.fromtimestamp(result['created']).strftime('%d/%m/%y')}")
        print(f"Last Modified: {datetime.datetime.fromtimestamp(result['modified']).strftime('%d/%m/%y')}")
    else:
        print("File not found.")

if __name__ == "__main__":
    main()