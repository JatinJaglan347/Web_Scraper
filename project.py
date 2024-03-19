# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the website you want to scrape
# url = 'https://kartikarora.co/'

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content of the webpage
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all the article titles using BeautifulSoup's find_all method
# article_titles = soup.find_all('div')

# # Extract and print the titles
# for title in article_titles:
#     print(title.text.strip())



import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://kartikarora.co/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Create a set to store unique content from div tags
unique_content = set()

# Find all div tags using BeautifulSoup's find_all method
div_elements = soup.find_all('h1')

# Loop through each div element
for div in div_elements:
    # Extract the text content of the div and strip whitespace
    content = div.text.strip()

    # Check if the content is not empty and not already in the unique_content set
    if content:
        unique_content.add(content)

# Print the unique content from div tags
for content in unique_content:
    print(content)
