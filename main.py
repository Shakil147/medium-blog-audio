import requests
from bs4 import BeautifulSoup
import pyttsx3,PyPDF2
import re
import os

# URL of the web page you want to scrape
url = "https://medium.com/@unseenjapan/japan-struggles-to-find-solutions-to-overtourism-0bb3aaefa001"  # Replace with the URL you want to scrape

def string_to_slug(input_string):
    # Convert the string to lowercase
    input_string = input_string.lower()

    # Remove special characters, leaving only alphanumeric and spaces
    input_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

    # Replace spaces with underscores
    input_string = input_string.replace(' ', '_')

    return input_string

def text_to_mp3(clean_text,title):
    print(title)
    slug = string_to_slug(title)
    output_folder = f"./{slug}"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(f"{output_folder}/{slug}.text", 'w',encoding='utf-8') as file:
        file.write(clean_text)

    output_file = f"{output_folder}/{slug}.mp3"
    speaker = pyttsx3.init()
    speaker.save_to_file(clean_text, output_file)
    speaker.runAndWait()
    speaker.stop()
    print("Audio created Successfully For: "+title,"Dile Name :"+output_file)

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open("./sdsd.html", 'w',encoding='utf-8') as file:
        file.write(response.text)
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find("section")

    # Now you can work with the parsed HTML content
    # For example, let's print the title of the web page
    title = soup.find(attrs={"data-testid": "storyTitle"})
    text_to_mp3(result.text.strip(),title.text)
    # You can extract other elements from the page as needed

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")



