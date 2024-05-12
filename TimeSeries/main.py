import pandas
import numpy
import matplotlib
import matplotlib.pyplot as pyplot
import seaborn
import warnings


df = pandas.read_csv("./data/Index2018.csv")

print( df.head() )
print( df.isna().sum() )

df.spx.plot(figsize=(20,5), title = "S&P500 Prices")
pyplot.show()

df.ftse.plot(figsize=(20,5), title = "FTSE100 Prices")
pyplot.show()

df.spx.plot(figsize=(20,5), title = "S&P500 Prices")
df.ftse.plot(figsize=(20,5), title = "FTSE100 Prices")
pyplot.title("S&P vs FTSE")
pyplot.show()

df.date = pandas.to_datetime(df.date, dayfirst = True)
print( df.head() )

df.set_index("date", inplace=True)
print( df.head() )

df.spx.plot(figsize=(20,5))
pyplot.title("S&P Prices", size = 24)
pyplot.show()

df.spx.plot(figsize=(20,5), title = "S&P500 Prices")
df.ftse.plot(figsize=(20,5), title = "FTSE100 Prices")
pyplot.title("S&P vs FTSE")
pyplot.show()