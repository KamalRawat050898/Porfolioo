import requests
from bs4 import BeautifulSoup

def check_amount_presence"https://www.airtel.in/dth-recharge':
    # Send GET request to the specified URL
    response = requests.get"https://www.airtel.in/dth-recharge"
    soup = BeautifulSoup(response.text, "html.parser")

    # Check if the webpage contains an element with class 'amount'
    amount_element = soup.find("div", class_="amount")

    if amount_element:
        print("Found: Amount is present on the webpage")
    else:
        print("Not found: Amount is not present on the webpage")

def main():
    # Path to the file containing URL
    file_path = "data/url.txt"

    # Read URL from the file
    with open(file_path, "r") as file:
        url = file.readline().strip()

    # Check if amount is present on the webpage
    check_amount_presence(url)

if __name__ == "__main__":
    main()
