# BAD STOCK TRADING APP - DO NOT USE IN REAL LIFE

"""
A simple stock market trading simulation game.

This program allows users to buy and sell stocks with simulated price fluctuations.
Not intended for actual trading - for educational/entertainment purposes only.
"""

import random

stocks = {
    "AAPL": 150,
    "GOOG": 2800,
    "TSLA": 720,
    "AMZN": 3400
}

portfolio = {}
money = 10000
def show_menu():
    """
    Displays the main menu options for the stock trading simulation game.
    """
    print("1. View Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Exit")

def view_stocks() -> None:
    """
    Updates each stock's price with a random fluctuation and displays the new prices.
    
    Each stock price is adjusted by a random percentage between -5% and +5%, ensuring the price does not fall below 1.
    """
    for stock, price in stocks.items():
        # More realistic fluctuation as a percentage of price
        fluctuation = price * random.uniform(-0.05, 0.05)
        new_price = max(1, round(price + fluctuation, 2))  # Ensure price stays positive
        stocks[stock] = new_price
        print(f"{stock}: ${new_price}")
def buy_stock():
    """
    Processes the purchase of shares for a selected stock if sufficient funds are available.
    
    Prompts the user to choose a stock and quantity to buy, deducts the total cost from available cash if affordable, and updates the portfolio with the purchased shares. Prints a confirmation message on success or an error message if funds are insufficient.
    """
    global money
    stock = input("Which stock do you want to buy? ")
    qty = int(input("How many shares? "))
    cost = stocks[stock] * qty
    if money >= cost:
        money -= cost
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty
        print(f"Bought {qty} shares of {stock}")
    else:
        print("You broke.")

def sell_stock():
    """
    Sells a specified quantity of owned stock and updates cash and portfolio.
    
    Prompts the user to enter a stock symbol and the number of shares to sell. If the user owns enough shares, the shares are sold at the current price, cash is increased, and the portfolio is updated. Otherwise, notifies the user of insufficient holdings.
    """
    global money
    stock = input("Which stock do you want to sell? ")
    qty = int(input("How many shares? "))
    if stock in portfolio and portfolio[stock] >= qty:
        money += stocks[stock] * qty
        portfolio[stock] -= qty
        print(f"Sold {qty} shares of {stock}")
    else:
        print("You don’t own that much.")

def view_portfolio():
    """
    Displays the user's current stock holdings and available cash balance.
    """
    print("Your portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares")
    print(f"Cash: ${money}")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        view_stocks()
    elif choice == "2":
        buy_stock()
    elif choice == "3":
        sell_stock()
    elif choice == "4":
        view_portfolio()
    elif choice == "5":
        print("k bye")
        break
    else:
        print("wat")
