import os
import sys
import shutil
import concurrent.futures

def process_directory(source_dir, destination_dir):
    def copy_file(file_path):
        _, file_name = os.path.split(file_path)
        file_extension = os.path.splitext(file_name)[1][1:]

        extension_dir = os.path.join(destination_dir, file_extension)
        os.makedirs(extension_dir, exist_ok=True)

        shutil.copy(file_path, extension_dir)

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(copy_file, file_path)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py source_dir [destination_dir]")
        sys.exit(1)

    source_dir = sys.argv[1]
    destination_dir = './dist' if len(sys.argv) < 3 else sys.argv[2]
    process_directory(source_dir, destination_dir)

if __name__ == "__main__":
    main()
