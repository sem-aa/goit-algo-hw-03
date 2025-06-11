import os
import sys
import shutil

def copyFolder (folder_path, new_folder, indent = 0):
    try:
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
        
            if os.path.isfile(file_path):
                print("  " * indent + f"File: {filename}")
                _, ext = os.path.splitext(filename)
                ext = ext[1:] if ext.startswith('.') else ext

                new_folder_path = os.path.join(new_folder, ext)
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)

                
                shutil.copy2(file_path, new_folder_path) 

        
            elif os.path.isdir(file_path):
                print("  " * indent + f"Folder: {filename}")

                copyFolder(file_path, new_folder, indent + 1)

    except FileNotFoundError:
        print("Folder not found")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Use: python main.py <path_to_folder> [destination_folder]")
        sys.exit(1)

    folder_path = sys.argv[1]
    new_folder = sys.argv[2] if len(sys.argv) > 2 else "dist" 
    copyFolder(folder_path, new_folder)