import requests
from bs4 import BeautifulSoup

website_url = "https://quotes.toscrape.com/"
# Make a GET request to fetch the raw HTML content from the website
response = requests.get(website_url)
#print(response.text)  # shows all website content

# We can also scrape quotes based on specific keywords
keywords = ['life', 'love', 'inspirational', 'humor', 'books', 'reading',
            'friendship', 'friends', 'truth', 'simile']

# Parse the HTML content
soup = BeautifulSoup(response.text, 'lxml')   # used lxml parser to parse the html content
quotes = soup.find_all('div', class_='quote')
#print(quotes)  # shows all quotes in the website with html tags

# Extract and print the text and author of each quote
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text  # span is used to get only text part
    
    if any(keyword in text.lower() for keyword in keywords):  # lowercase because keywords are lowercase
        # to check if any keyword is present in the quote
        print(f'{text}  - {author}')
