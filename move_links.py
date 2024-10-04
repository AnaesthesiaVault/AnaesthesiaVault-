import os
import re

# Define the path to your Obsidian vault (update with your correct path)
vault_path = r"C:\Users\fuys2\OneDrive\Uys Drive\Uys Obsidian Vault\Anaesthesia core notes"

# Regular expression to match YAML frontmatter
yaml_regex = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

print(f"Looking for markdown files in: {vault_path}")

# Check if the vault directory exists
if not os.path.exists(vault_path):
    print(f"Error: The path {vault_path} does not exist.")
else:
    # Loop through all markdown files in the vault
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # Print file being processed
                print(f"\nProcessing: {file_path}")
                
                try:
                    # Read the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Find YAML frontmatter
                    match = yaml_regex.search(content)
                    if match:
                        frontmatter = match.group(1)
                        print(f"Frontmatter found in {file_path}:\n{frontmatter}")

                        # Extract the 'Links' property if it exists (handles quoted links)
                        links_match = re.search(r"Links:\s*\n(.*?)(\n\s*\n|$)", frontmatter, re.DOTALL)
                        if links_match:
                            links = links_match.group(1).strip()
                            print(f"Links section found:\n{links}")
                            
                            # Convert YAML links to markdown format (handle quoted links)
                            markdown_links = ""
                            for link in re.findall(r'- "?\[\[(.*?)\]\]"?', links):
                                markdown_links += f"- [[{link}]]\n"
                            print(f"Formatted Links:\n{markdown_links}")

                            # Remove the 'links' section from the YAML
                            updated_frontmatter = re.sub(r"Links:\s*\n(.*?)(\n\s*\n|$)", '', frontmatter, flags=re.DOTALL).strip()
                            print(f"Updated Frontmatter:\n{updated_frontmatter}")
                            
                            # Update the content: Remove the old YAML and move links to the body
                            updated_content = re.sub(yaml_regex, f"---\n{updated_frontmatter}\n---", content)
                            
                            # Append the extracted links to the end of the note under "# Links" section
                            if markdown_links:
                                updated_content += f"\n# Links\n{markdown_links}"

                            # Write the updated content back to the file
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(updated_content)
                            
                            # Print success message
                            print(f"Updated {file_path}")
                        else:
                            print(f"No links found in {file_path}.")
                    else:
                        print(f"No frontmatter found in: {file_path}")
                
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
