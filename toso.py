import os
import shutil

# Flush the DNS Resolver Cache
os.system("ipconfig /flushdns")

# Check for errors on the hard drive
os.system("chkdsk")

# Scan for and repairs corrupt system files
os.system("sfc /scannow")

# Folder paths that will get their content deleted
folder_paths = "/Users/user/AppData/Local/Temp", # Cleans the temporary files created by applications 
                "/Users/user/Pictures/Screenshots", # Cleans the screenshots made using the WIN + SHIFT + S shortcut
                "/Users/user/AppData/Local/CrashDumps", # Cleans the applications' crash dumps
                "/$Recycle.Bin/S-1-5-21-4083530894-3095089788-2986954845-1003" # Cleans the recycle bin

for folder_path in folder_paths:
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Get the contents of the folder
        folder_contents = os.listdir(folder_path)
        # Loop through each item in the folder
        for item in folder_contents:
            # Get the full path of the item
            item_path = os.path.join(folder_path, item)
            try:
                # If the item is a file, delete it
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"Successfully deleted file: {item_path}")
                # If the item is a directory, delete it recursively
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Successfully deleted directory: {item_path}")
            # Catch any OSError exceptions that occur during the deletion process
            except OSError as e:
                print(f"Error deleting file: {item_path}. {e}")
    # Print an error message if the folder does not exist
    else:
        print(f"Folder does not exist: {folder_path}")
