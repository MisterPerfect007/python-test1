from flask import *
import json



""" url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'

def main():
    resp = requests.get(url).json()
    return json.dumps(resp)

main() """

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    data = {'name': 'perfect'}
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
    