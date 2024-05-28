import asciichartpy as acp
from decimal import Decimal
import requests
import argparse

parser = argparse.ArgumentParser(description="Euro")
parser.add_argument("--days", dest="days", type=int, help="Number of days", default=30)
parser.add_argument("--height", dest="height", type=int, help="Height of the chart", default=10)
args = parser.parse_args()

url = f"https://economia.awesomeapi.com.br/json/daily/EUR/{args.days}"

euro = requests.get(url)
ask = [Decimal(day["ask"]) for day in euro.json()[-1::-1]]

print(acp.plot(ask, {"height": args.height}))
print(f"Last: {ask[-2]:.2f} - Now: {ask[-1]:.2f}")
