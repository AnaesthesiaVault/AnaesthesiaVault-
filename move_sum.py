import os
import re

def move_and_rename_summary_to_top(file_path):
    print(f"Processing file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Identify metadata block if it exists (YAML frontmatter between `---`)
    metadata_match = re.search(r'^---[\s\S]*?---\s*', content)
    if metadata_match:
        metadata_end = metadata_match.end()
        metadata = content[:metadata_end]
        rest_of_note = content[metadata_end:]
        print("Found metadata")
    else:
        metadata = ''
        rest_of_note = content
        print("No metadata found")

    # Identify the **References:** section with markdown bold
    references_match = re.search(r'(?i)\*\*References:?\*\*\s*[\s\S]*?\n', rest_of_note)
    if references_match:
        references_end = references_match.end()
        before_references = rest_of_note[:references_end]
        after_references = rest_of_note[references_end:]
        print("Found References section")
    else:
        before_references = rest_of_note
        after_references = ''
        print("No References section found")

    # Look for the summary section right after the references, with markdown bold
    summary_match = re.search(r'(?i)\*\*(Summary|Summaries?|Summary\s*or\s*mind\s*map|Summaries?\s*or\s*mind\s*maps?)\*\*\s*([\s\S]*?)\n---+', after_references)
    
    if summary_match:
        summary_start = summary_match.start()
        summary_section = after_references[summary_start:]
        print("Found Summary section")
        # Rename the summary heading to "Summaries"
        summary_section = re.sub(r'(?i)\*\*(Summary|Summaries?|Summary\s*or\s*mind\s*map|Summaries?\s*or\s*mind\s*maps?)\*\*', '**Summaries**', summary_section)
        after_references = after_references[:summary_start]
    else:
        print("No Summary section found")
        return

    # Prepare the new content with summary moved to the top
    new_content = metadata + '\n' + summary_section + '\n\n' + before_references + after_references
    
    # Write back the changes to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"Successfully processed file: {file_path}")

# Path to the directory containing the markdown files
directory_path = r'C:\Users\Francois Uys\OneDrive\Uys Drive\Uys Obsidian Vault\Anaesthesia core notes'

# Process all markdown files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.md'):
        file_path = os.path.join(directory_path, filename)
        move_and_rename_summary_to_top(file_path)

print("Summary sections have been successfully moved and renamed!")
