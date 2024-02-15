import csv
import requests
from bs4 import BeautifulSoup

def extract_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    issue_items = soup.find_all('div', class_='issue-item__content')

    extracted_data = []
    for issue_item in issue_items:
        title_element = issue_item.find('h5', class_='issue-item__title').find('a')
        title = title_element.get_text(strip=True)
        citation_element = issue_item.find('span', class_='citation')
        citation = citation_element.get_text(strip=True) if citation_element else ''

        extracted_data.append({'Title': title, 'Citation': citation})

    return extracted_data

def append_to_csv(entries, output_file='citation.csv'):
    fieldnames = ['Title', 'Citation']

    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        for entry in entries:
            writer.writerow(entry)

if __name__ == "__main__":
    # Replace 'your_url_here' with the actual URL of the HTML page
    url = 'https://dl.acm.org/doi/proceedings/10.1145/3567955'
    
    # Fetch HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    extracted_data = extract_info(html_content)
    append_to_csv(extracted_data)
    print("Data appended to CSV file.")

