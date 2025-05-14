# for i in range(2):
#     print(i)
#
# for j in range (5):
#     print(j)

# Output is on a new line for each of the first outcome 0,1.
# Then there is the secons, 0, 1, 2, 3, 4 on their own lines

# for i in range(2):
#     for j in range(5):
#         print(j)
# this prints (on seperate lines) 0 1 2 3 4 0 1 2 3 4
# it is printing the second range(5) twice,
# because there are 2 elements in the first range
# first loop is range(2)[0], second is range(2)[1]

# to see this better:
# for i in range(2):
#     for j in range(5):
#         print([i,j])
"""
first column is i, second is j
[0, 0] is [i[0], j[0]]
[0, 1] is [i[0], j[1]] etc
[0, 2]
[0, 3]
[0, 4]
[1, 0]
[1, 1]
[1, 2]
[1, 3]
[1, 4]
"""

# products = ['Product A', 'Product B']
# exp_sales = [10000, 11000, 12000, 13000, 14000]
#
# for i in products:
#     for j in exp_sales:
#         print([i,j])

# Triple Nested For Loops

products = ['Product A', 'Product B']
exp_sales = [10000, 11000, 12000, 13000, 14000]
time_horizon = (1, 3, 12)
#
# for prod in products:
#     for sale in exp_sales:
#         for t_hor in time_horizon:
#             print('Expected sales for a period of {0} month(s) for {1}: ${sales}.'.format(t_hor, prod, sales = sale*t_hor))
#
# # same result, different order
#
# for prod in products:
#     for t_hor in time_horizon:
#         for sale in exp_sales:
#             print('Expected sales for a period of {0} month(s) for {1}: ${sales}.'.format(t_hor, prod, sales = sale*t_hor))

# print((lambda x: (2+5*x**4)**2/(x+3)**3) (2))
print((lambda x,y: x+y) (2,3))