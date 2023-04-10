import ctypes, os, sys, shutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        raise RuntimeError("Admin check not supported on this platform.")

def main():
    # Folder paths that will get their content deleted
    folder_paths = [
        "C:/Users/noxtg/Pictures/Screenshots", # Cleans the screenshots made using the WIN + SHIFT + S shortcut
        "C:/Users/noxtg/AppData/Local/Temp", # Cleans the temporary files created by applications 
        "C:/Users/noxtg/AppData/Local/CrashDumps" # Cleans the applications' crash dumps
    ]

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
    
    # Flush the DNS Resolver Cache
    os.system("ipconfig /flushdns")

    # Scan for and repairs corrupt system files (requires admin privileges)
    os.system("sfc /scannow")

    # Check for errors on the hard drive (requires admin privileges)
    os.system("chkdsk")

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        # Re-run the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW( None, "runas", sys.executable, f'"{__file__}"', None, 1 )
