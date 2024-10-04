import os

# Set the path to your Obsidian vault (update this to your specific vault path)
vault_path = r"C:\Users\fuys2\OneDrive\Uys Drive\Uys Obsidian Vault\Anaesthesia core notes"

# Function to rename files by removing the "_temp" suffix
def revert_filenames(vault_path):
    # Loop through all markdown files in the vault directory
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith("_temp.md"):
                file_path = os.path.join(root, file)
                # Create the new file path by removing "_temp" suffix
                new_file_path = file_path.replace("_temp.md", ".md")

                # Rename the file to revert to its original name
                os.rename(file_path, new_file_path)
                print(f"Reverted: {file} to {os.path.basename(new_file_path)}")

# Call the function to revert all file names
revert_filenames(vault_path)
