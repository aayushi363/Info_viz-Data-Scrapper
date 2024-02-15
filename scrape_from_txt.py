import csv
import re

def extract_info(file_content):
    entries = []
    current_entry = {}

    for line in file_content.split('\n'):
        match_author = re.match(r'\s*author\s*=\s*\{(.+?)\}', line, re.DOTALL)
        match_title = re.match(r'\s*title\s*=\s*\{(.+?)\}', line, re.DOTALL)
        match_year = re.match(r'\s*year\s*=\s*\{(.+?)\}', line, re.DOTALL)
        match_abstract = re.match(r'\s*abstract\s*=\s*\{(.+?)\}', line, re.DOTALL)
        match_keywords = re.match(r'\s*keywords\s*=\s*\{(.+?)\}', line, re.DOTALL)

        if match_author:
            current_entry['Author'] = extract_multiline_content(match_author.group(1))

        if match_title:
            current_entry['Title'] = extract_multiline_content(match_title.group(1))

        if match_year:
            current_entry['Year'] = extract_multiline_content(match_year.group(1))

        if match_abstract:
            current_entry['Abstract'] = extract_multiline_content(match_abstract.group(1))

        if match_keywords:
            current_entry['Keywords'] = extract_multiline_content(match_keywords.group(1))
            entries.append(current_entry)
            current_entry = {}

    return entries

def extract_multiline_content(content):
    # Function to join multiline content into a single line
    return ' '.join(line.strip() for line in content.split('\n'))

# Read the content from the file
with open('asplos.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Extract information
entries = extract_info(text)

# Append to CSV file with header
csv_filename = 'asplos_data.csv'
fieldnames = ['Author', 'Title', 'Year', 'Abstract', 'Keywords']

with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header if the file is empty
    if csvfile.tell() == 0:
        writer.writeheader()

    for entry in entries:
        writer.writerow(entry)

print(f"CSV file '{csv_filename}' updated successfully.")

