import pandas as pd
names = pd.Series(["Martin Peterson", "John Fitzpatrick", "Kate Cruz"])
last_names = names.str.split().str[1]
print(last_names)
print(type(last_names))
