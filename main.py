finance= {}
def add_transaction(finance: dict):
    result_balance = 0
    balance = int(input("balance: "))
    date = input("date: YY/MM/DD: ")
    while True:
        direction = input("direction: buy/sell: ")
        if direction == "buy" or direction == "sell":
            break
        print("Enter only buy or sell: ")
    while True:
        category = str(input("category: forex/crypto/index: "))
        if category == "forex" or category == "crypto" or category == "index":
            break
        print("Enter only forex or crypto or index: ")
    while True:
        result = str(input("result: s/l or t/p "))
        if result == "s/l" or result == "t/p":
            break
        print("Enter only s/l or t/p: ")
    amount = int(input("amount: "))
    transaction_id = int(input("transaction_id: "))
    if result == "s/l":
        result_balance = balance - amount
    elif result == "t/p":
        result_balance = balance + amount
    finance[transaction_id] = {
        "balance": result_balance,
        "date": date,
        "result": result,
        "dir": direction,
        "category": category,
        "amount": amount
    }
    print("Transaction added!")
    print()
    print("Transaction id:", transaction_id)
    print("Direction:", finance[transaction_id]["dir"])
    print("Date:", finance[transaction_id]["date"])
    print("Category:", finance[transaction_id]["category"])
    print("Result:", finance[transaction_id]["result"])
    print("Amount:", finance[transaction_id]["amount"])
    print("Balance:", finance[transaction_id]["balance"])
    print()


def delete_transaction(finance: dict):
    transaction_id = int(input("transaction_id: "))
    if transaction_id in finance:
        del finance[transaction_id]
        print("Transaction deleted!")
    else:
        print("Transaction not found!")


def check_transactions(finance: dict) -> int:
    for v, k in finance.items():
        print(v, k)


def main():
    while True:
        print("1. - add transaction")
        print("2. - delete transaction")
        print("3. - check transactions")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_transaction(finance)
        elif choice == "2":
            delete_transaction(finance)
        elif choice == "3":
            check_transactions(finance)
        else:
            print("Invalid choice")
main()