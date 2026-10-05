import requests


class CryptoCurrency:

    @staticmethod
    def check_the_currencies() ->dict[str, float]:
        currencies = ["BTC", "ETH", "BNB", "SOL", "XRP"]
        prices = {}
        for coin in currencies:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
            response = requests.get(url)
            data = response.json()
            prices[coin] = data["price"]
        return prices

    @staticmethod
    def chosen_currency(coin) ->dict[str, float]:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT"
        response = requests.get(url)
        data = response.json()
        return data["price"]


def main():
    print("1 — main currencies")
    print("2 — choose a currency")
    choice = input("Choose the option: ")
    if choice == "1":
        print(CryptoCurrency.check_the_currencies())
    elif choice == "2":
        coin = input("type the currency: ")
        print(CryptoCurrency.chosen_currency(coin))
    else:
        print("Wrong input")
main()