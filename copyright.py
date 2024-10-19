import os

# Define the directory path to your Obsidian vault
vault_path = r'C:\Users\Francois Uys\OneDrive\Uys Drive\Uys Obsidian Vault'  # Using raw string for Windows paths

# Define the copyright disclaimer
disclaimer = "\n\n---\n\n**Copyright**\n© 2022 Francois Uys. All Rights Reserved.\n"

# Function to append the disclaimer to each .md file
def add_disclaimer_to_notes(vault_directory):
    for root, dirs, files in os.walk(vault_directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # Open the file and check if the disclaimer is already added
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()  # Remove any trailing whitespace/newlines
                
                # If the disclaimer is not already present at the end, append it
                if not content.endswith(disclaimer.strip()):
                    with open(file_path, 'a', encoding='utf-8') as f:
                        f.write(disclaimer)

# Run the function on your vault path
add_disclaimer_to_notes(vault_path)

print("Disclaimer has been added to all notes.")
