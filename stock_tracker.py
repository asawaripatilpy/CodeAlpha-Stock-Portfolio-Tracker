# ============================================
#        STOCK PORTFOLIO TRACKER
# ============================================

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 160,
    "AMZN": 190
}

# Portfolio list
portfolio = []


# ============================================
# Add Stock Function
# ============================================

def add_stock():

    print("\n---------- ADD STOCK ----------")

    print("\nAvailable Stocks:")

    for stock, price in stock_prices.items():
        print(f"{stock:<8} : ${price}")

    stock_name = input("\nEnter stock symbol: ").upper()

    # Check stock
    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.")
        return

    # Get quantity
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    price = stock_prices[stock_name]

    investment = price * quantity

    # Add stock to portfolio
    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print("\n✅ Stock added successfully!")
    print(f"Stock       : {stock_name}")
    print(f"Quantity    : {quantity}")
    print(f"Price       : ${price}")
    print(f"Investment  : ${investment}")


# ============================================
# View Portfolio Function
# ============================================

def view_portfolio():

    print("\n==============================================")
    print("              YOUR PORTFOLIO")
    print("==============================================")

    if len(portfolio) == 0:
        print("Your portfolio is empty.")
        print("==============================================")
        return

    total_investment = sum(
        item["investment"] for item in portfolio
    )

    print(
        f"{'Stock':<10}"
        f"{'Quantity':<10}"
        f"{'Price':<10}"
        f"{'Investment':<12}"
        f"{'Share %'}"
    )

    print("----------------------------------------------")

    for item in portfolio:

        percentage = (
            item["investment"] / total_investment
        ) * 100

        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<10}"
            f"${item['price']:<9}"
            f"${item['investment']:<11}"
            f"{percentage:.2f}%"
        )

    print("----------------------------------------------")

    print(f"TOTAL INVESTMENT VALUE: ${total_investment}")

    print("==============================================")


# ============================================
# Save Portfolio as TXT
# ============================================

def save_txt():

    if len(portfolio) == 0:
        print("\n❌ Portfolio is empty. Add stocks first.")
        return

    total_investment = sum(
        item["investment"] for item in portfolio
    )

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=======================\n\n")

        for item in portfolio:

            file.write(
                f"Stock: {item['stock']} | "
                f"Quantity: {item['quantity']} | "
                f"Price: ${item['price']} | "
                f"Investment: ${item['investment']}\n"
            )

        file.write(
            f"\nTotal Investment Value: ${total_investment}\n"
        )

    print("\n✅ Portfolio saved successfully as portfolio.txt")


# ============================================
# Save Portfolio as CSV
# ============================================

def save_csv():

    if len(portfolio) == 0:
        print("\n❌ Portfolio is empty. Add stocks first.")
        return

    total_investment = sum(
        item["investment"] for item in portfolio
    )

    with open("portfolio.csv", "w") as file:

        file.write("Stock,Quantity,Price,Investment\n")

        for item in portfolio:

            file.write(
                f"{item['stock']},"
                f"{item['quantity']},"
                f"{item['price']},"
                f"{item['investment']}\n"
            )

        file.write(
            f"Total,,, {total_investment}\n"
        )

    print("\n✅ Portfolio saved successfully as portfolio.csv")


# ============================================
# Main Program
# ============================================

while True:

    print("\n")
    print("╔══════════════════════════════════════╗")
    print("║       📈 STOCK PORTFOLIO TRACKER     ║")
    print("╚══════════════════════════════════════╝")

    print("\n1. Add Stock")
    print("2. View Portfolio")
    print("3. Save Portfolio as TXT")
    print("4. Save Portfolio as CSV")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":

        add_stock()

    elif choice == "2":

        view_portfolio()

    elif choice == "3":

        save_txt()

    elif choice == "4":

        save_csv()

    elif choice == "5":

        print("\n===================================")
        print("Thank you for using Stock Portfolio Tracker!")
        print("===================================")
        break

    else:

        print("\n❌ Invalid choice. Please enter a number from 1 to 5.")