import requests
import mysql.connector
import json

## Connects to mySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="AaBbCc123",
    database="stocks"
)

mycursor = mydb.cursor()

## Handles API Calls
def api(symbol):
    request = 'https://cloud.iexapis.com/stable/stock/' + symbol + '/quote?token=pk_c37812d235954d52b6089fe8ecf50261'
    return request

## Presents JSON from API in a user-friendly format
def jsonToStock(jsonObj):
    stockDict = json.loads(jsonObj)
    print("Symbol:", stockDict["symbol"])
    print("Price:", stockDict["latestPrice"])
    print("Company Name:", stockDict["companyName"])
    print("--------------------")


end = False


# Loop contains controls for program
while end is False:
    print("1. Save a stock symbol")
    print("2. View saved stocks")
    print("3. Remove stock symbols")
    print("4. View Stock Prices")
    print("5. Terminate")
    print("Enter a command")
    command = int(input())

    if command == 1:
        print("Enter a stock symbol")
        stockSymbol = input()
        mycursor.execute("INSERT INTO symbols VALUES ('" + stockSymbol + "');")
        mydb.commit()
        print(stockSymbol, "has been successfully added to the database.")

    if command is 2:
        mycursor.execute("SELECT * FROM symbols")
        results = mycursor.fetchall()
        for row in results:
            print(row)

    if command is 3:
        print("Enter the name of the stock you want to remove")
        symbolName = input()
        mycursor.execute("DELETE FROM symbols WHERE symbolName='" + symbolName + "';")
        mydb.commit()
        print(symbolName, "has been successfully added to the database.")

    if command is 4:
        stocks = []
        mycursor.execute("SELECT * FROM symbols")
        results = mycursor.fetchall()
        for row in results:
            stocks.append(row[0])
        for stock in stocks:
            r = requests.get(api(stock))
            jsonToStock(r.content)

    if command is 5:
        end = True
    else:
        print('Enter a valid command')