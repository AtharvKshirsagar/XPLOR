import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://www.fabhotels.com/blog/places-to-visit-in-mumbai/"
response = requests.get(url)

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the section containing the places to visit
places_section = soup.find("section", class_="blog-entry-content")

# Find all the individual place entries
place_entries = places_section.find_all("div", class_="place-entry")

# Initialize empty lists for storing the scraped data
data = []

# Iterate over each place entry and extract relevant information
for place in place_entries:
    name = place.find("h4", class_="entry-title").text.strip()
    description = place.find("div", class_="entry-description").text.strip()
    image_link = place.find("img")["src"]
    link = place.find("a", class_="btn")["href"]
    
    # Append the extracted data to the list
    data.append([name, description, image_link, link])

# Create a DataFrame from the scraped data
df = pd.DataFrame(data, columns=["Name", "Description", "Image Link", "Link"])

# Print the DataFrame
print(df)
