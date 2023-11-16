import requests
import csv
import time
from datetime import datetime

# Function to make the API call and store response in CSV
def make_api_call_and_save():
    url = "https://dummyjson.com/products/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Get current timestamp for filename and CSV row
        current_time = datetime.now().strftime("%Y%m%d-%H%M%S")

        # Parsing response JSON
        data = response.json()

        # Writing data to CSV
        with open("products.csv", "a", newline="") as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=data.keys())

            # If file is empty, write header
            if csvfile.tell() == 0:
                csvwriter.writeheader()

            csvwriter.writerow(data)
            print(f"{current_time} Status code: {response.status_code}")

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Run the script every hour
while True:
    make_api_call_and_save()
    # Sleep for an hour (3600 seconds)
    time.sleep(3)
