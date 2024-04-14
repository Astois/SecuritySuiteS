import os

def get_file_size(file_path):
    return os.path.getsize(file_path)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def count_files_and_bytes(directory):
    file_count = 0
    total_bytes = 0
    file_extension_bytes = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_count += 1
            file_size = get_file_size(file_path)
            total_bytes += file_size

            file_extension = get_file_extension(file)
            if file_extension not in file_extension_bytes:
                file_extension_bytes[file_extension] = 0
            file_extension_bytes[file_extension] += file_size

    return file_count, total_bytes, file_extension_bytes

def main():
    directory = input("Enter the directory path: ")
    while not os.path.isdir(directory):
        print("Invalid directory path. Please try again.")
        directory = input("Enter the directory path: ")

    file_count, total_bytes, file_extension_bytes = count_files_and_bytes(directory)

    print(f"\nTotal number of files: {file_count}")
    print(f"Total number of bytes used by all files: {total_bytes}")

    print("\nBreakdown of the number of bytes used by files with common file extensions:")
    for extension, bytes_used in file_extension_bytes.items():
        print(f"{extension}: {bytes_used} bytes")

if __name__ == "__main__":
    main()