#  pyramid star pattern

# Total number of rows
rows = 5

for i in range(1, rows + 1):
   
    print(' ' * (rows - i), end='') # print spaces

    print('*' * (2 * i - 1)) # print stars
