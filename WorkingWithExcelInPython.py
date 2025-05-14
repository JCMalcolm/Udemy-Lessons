import numpy as np

np.set_printoptions(suppress= True, linewidth= 150)
# print(np.loadtxt('Lending-Company-Total-Price.csv', delimiter=',', dtype = str))
# print(np.genfromtxt('Lending-Company-Total-Price.csv', delimiter=','))
print(np.genfromtxt('Lending-Company-Total-Price.csv',
                    delimiter=',',
                    dtype= np.str_,
                    skip_header = 1,
                    skip_footer= 15,
                    usecols= (1,2,4),
                    comments='#',
                    converters= {3: lambda s: float(s or 0)},
                    missing_values='missing',
                    autostrip=True))
