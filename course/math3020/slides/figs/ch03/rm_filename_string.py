import os

def remove_string_from_filenames(folder_path, string_to_remove):
    """
    Scans a folder and removes a specific string from all file names.
    """
    # Verify the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return

    files_renamed = 0

    # Iterate through all files in the specified directory
    for filename in os.listdir(folder_path):
        # Check if the target string is in the current filename
        if string_to_remove in filename:
            
            # Generate the new filename by replacing the target string with nothing
            new_filename = filename.replace(string_to_remove, "")
            
            # Construct the full absolute paths for the rename operation
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            try:
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                files_renamed += 1
            except FileExistsError:
                print(f"Skipped: '{new_filename}' already exists in this folder.")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")
                
    print(f"\nProcess complete. Successfully renamed {files_renamed} files.")

# --- Configuration ---
# 1. Replace with the actual path to your folder (use raw string 'r' for Windows paths)
target_folder = r"."

# 2. Replace with the exact string you want to remove. 
# Note: Include the space if you are trying to remove " (1)" entirely.
target_string = " 8" 

# Run the function
remove_string_from_filenames(target_folder, target_string)