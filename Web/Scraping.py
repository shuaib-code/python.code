import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://aoiacademy.com/all-course/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all course titles (you might need to adjust the selector based on the actual HTML structure)
    course_titles = soup.find_all('h2', class_='course-title')

    # Print out the course titles
    for title in course_titles:
        print(title.text.strip())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
