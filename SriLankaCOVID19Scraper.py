import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.hpb.health.gov.lk/en"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the elements containing the COVID-19 data
    data_elements = soup.find_all("h4", {"class": "count", "data-counter": True})

    # Extract and print the required data
    if data_elements:
        total_confirmed_cases = data_elements[0].text.strip()
        active_cases = data_elements[1].text.strip()
        daily_new_cases = data_elements[2].text.strip()
        recovered_cases = data_elements[3].text.strip()
        deaths = data_elements[4].text.strip()

        print("Total Confirmed Cases:", total_confirmed_cases)
        print("Active Cases:", active_cases)
        print("Daily New Cases:", daily_new_cases)
        print("Recovered Cases:", recovered_cases)
        print("Deaths:", deaths)
    else:
        print("Data elements not found.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)