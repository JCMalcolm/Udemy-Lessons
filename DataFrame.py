import pandas as pd

# 1. Construct a DataFrame from a dictionary of lists
# Note: no indexing specified, provided implicit default integer index
data = {'ProductName': ['Product A', 'Product B', 'Product C'],
        'ProductPrice': [22250, 16600, 12500]}
df = pd.DataFrame(data)
# print(df)

# 2. Construct a DataFrame from a dictionary of lists WITH index
df2 = pd.DataFrame(data, index=['A','B','C'])
# print(df2)
product_IDs = ['A','B','C']
df3 = pd.DataFrame(data, index= product_IDs)
# print(df3)

# 3. Construct a DataFrame from a list of dictionaries
data2 = [{'ProductName':'Product A', 'ProductPrice':22250},
         {'ProductName':'Product B', 'ProductPrice':16600},
         {'ProductName':'Product C', 'ProductPrice':12500}]
df4 = pd.DataFrame(data2)
# print(df4)

# 4. Construct a DataFrame from a dictionary of Pandas Series
# ser_products = pd.Series(['Product A', 'Product B', 'Product C'])
# ser_prices = pd.Series([22250, 16600, 12500])

# data3 = {'ProductName':ser_products, 'ProductPrice':ser_prices}
# df5 = pd.DataFrame(data3)
# print(df5)

ser_products = pd.Series(['Product A', 'Product B', 'Product C'], index = ['A','B','C'])
ser_prices = pd.Series([22250, 16600, 12500], index = ['A','B','C'])
# can assign index as separate variable to ensure matching
# pandas will match if second list was ['C','A','B'] but you get the wrong pairings
data3 = {'ProductName':ser_products, 'ProductPrice':ser_prices}
df5 = pd.DataFrame(data3)
# print(df5)

# 5. Construct a DataFrame from a list of lists
# The number of elements in each inner list must be fixed.
# Note: if you ['Product C', 12500, 5000], you'll get 3rd column and if no other entries have this, NaN
data4 = [['Product A', 22250], ['Product B', 16600], ['Product C', 12500]]
df6 = pd.DataFrame(data4)
# print(df6)
df6.columns = ['ProductName', 'ProductPrice']
df6.index = ['A','B','C']
# print(df6)

# 6. Construct a DataFrame in a Professional Way
# When constructing a DF, you need to provide Data, Columns, Index
# Use parameters pertaining to Pandas DataFrame method

dfLast = pd.DataFrame(data = [['Product A', 22250], ['Product B', 16600], ['Product C', 12500]],
                      columns = ['ProductName', 'ProductPrice'],
                      index = ['A','B','C'])
print(dfLast)
print(dfLast.shape)

