import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

# plt.style.use('_mpl-gallery')
# plt.show()
# Get the funds data
spy = yf.Ticker("SPY").funds_data
print(spy.description)
print(spy.top_holdings)
myportfolio = spy.top_holdings.index.tolist()
print(myportfolio)
# 1. Import the required libraries
start = dt.datetime(2025, 1, 1)
end = dt.datetime(2025, 4, 1)
df_portfolio = yf.download(myportfolio, start, end)
df_portfolio.to_excel("myportfolio2.xlsx")
print(df_portfolio.head(5))

# Get dividents for the stock
for stock in myportfolio:
    stock1 = yf.Ticker(stock)
    print("Dividends for ", stock)
    print(stock1.dividends)
    print(stock1.dividends.sum())
    plt.plot(df_portfolio["Close"][stock], label=stock)
plt.title("Stock Prices")
plt.xlabel("Date")
plt.legend()
plt.show()
