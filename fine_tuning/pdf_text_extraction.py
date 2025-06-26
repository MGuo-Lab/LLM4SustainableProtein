from pdfminer.high_level import extract_text
import re

# Specify paper filename (an example open-access paper is provided)
filename = 'example_paper_vaswani_2017.pdf'

# Extract text, using pdfminer
text = extract_text(filename)


# Function to split text by case-insensitive matches
def split_by_last_occurrence(text: str, substring: str) -> str:
    
    # Find all case-insensitive matches
    matches = list(re.finditer(re.escape(substring), text, re.IGNORECASE))
    
    # Check for matches and return split text, if so
    if matches:
        last_match = matches[-1]
        split_index = last_match.start()
        return text[:split_index]
    else:
        return text


# Attempt to cut down token count, by removing any text beyond references/bibliography
text = split_by_last_occurrence(text, 'references')
text = split_by_last_occurrence(text, 'bibliography')

# Checks for redundant "cid" occurences to remove (these can occur due to pdf formatting)
if 'cid:' in text:
    text = re.sub(r'\(cid:\d+\)', '', text)


# Specify output file name
output_file = 'example_paper_text.txt'

# Save extracted text to file
with open(output_file, 'w') as f:
    f.write(text)

