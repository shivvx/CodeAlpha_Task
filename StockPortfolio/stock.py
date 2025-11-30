#(Stock Prices)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 175
}
def main():
    print("--- Simple Stock Portfolio Tracker ---")
    print(f"Available stocks in system: {', '.join(stock_prices.keys())}")
    
    total_value = 0
    portfolio_log = []

    while True:
        stock_name = input("\nEnter stock symbol (or type 'DONE' to finish): ").upper()
        if stock_name == "DONE":
            break

        if stock_name in stock_prices:
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                
                cost = stock_prices[stock_name] * quantity
                total_value += cost

                entry = f"{stock_name}: {quantity} shares @ ${stock_prices[stock_name]} = ${cost}" #log
                portfolio_log.append(entry)
                print(f"-> Added. Current Total: ${total_value}")
                
            except ValueError:
                print("Error: Please enter a valid number for quantity.")
        else:
            print(f"Sorry, we don't have price data for {stock_name}.")

    print("\n" + "="*30)
    print(f"FINAL PORTFOLIO VALUE: ${total_value}")
    print("="*30)

    save_file = input("Would you like to save this result? (y/n): ").lower()
    
    if save_file == 'y':
        try:
            with open("portfolio_summary.txt", "w") as f:
                f.write("--- Portfolio Summary ---\n")
                for item in portfolio_log:
                    f.write(item + "\n")
                f.write("="*30 + "\n")
                f.write(f"TOTAL VALUE: ${total_value}\n")
            print("Success! Saved to 'portfolio_summary.txt'")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
