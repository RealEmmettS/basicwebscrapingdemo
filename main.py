# TARGET URL: https://forecast.weather.gov/MapClick.php?lat=32.7782&lon=-96.7951

# TARGET ELEMENTS: 
# - Temp in Fahrenhiet: <p class="myforecast-current-lrg">
# - Generalized Conditions: <p class="myforecast-current">
# - Location: <h2 class="panel-title">


import requests
from bs4 import BeautifulSoup

# TARGET URL
url = "https://forecast.weather.gov/MapClick.php?lat=32.7782&lon=-96.7951"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the temperature element
temp_element = soup.find("p", class_="myforecast-current-lrg")
temperature = temp_element.text.strip() if temp_element else "N/A"

# Find the generalized conditions element
conditions_element = soup.find("p", class_="myforecast-current")
conditions = conditions_element.text.strip() if conditions_element else "N/A"

# Find the location element
location_element = soup.find("h2", class_="panel-title")
location = location_element.text.strip() if location_element else "N/A"

# Display the current weather information
print(f"Current Weather at {location}: \n")
print(f"Temperature: {temperature}")
print(f"Conditions: {conditions}")