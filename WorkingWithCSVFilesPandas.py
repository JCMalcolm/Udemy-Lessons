import pandas as pd

file = 'Lending-company.csv'
# df = pd.read_csv(file)
# print(df)

# Changing the indexing column
df = pd.read_csv(file, index_col='LoanID')
print(df)

