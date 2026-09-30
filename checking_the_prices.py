import requests


class Crypto_Currency:

    def check_the_currencies(self):
        currencies = ["BTC", "ETH", "BNB", "SOL", "XRP"]
        prices = {}
        for coin in currencies:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
            response = requests.get(url)
            data = response.json()
            prices[coin] = data["price"]
        return prices


    def chosen_currency(self, coin):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT"
        response = requests.get(url)
        data = response.json()
        return data["price"]


def main():
    crypto = Crypto_Currency()
    print("1 — main currencies")
    print("2 — choose a currency")
    choice = input("Choose the option: ")
    if choice == "1":
        print(crypto.check_the_currencies())
    elif choice == "2":
        coin = input("type the currency: ")
        print(crypto.chosen_currency(coin))
    else:
        print("Wrong input")
main()