import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Somethings went wrong while requesting...")
    else:
        bitcoin_data = response.json()
        price = bitcoin * float(bitcoin_data["bpi"]["USD"]["rate"].replace(",", ""))
        print(f"${price:,.4f}")