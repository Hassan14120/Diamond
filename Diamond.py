num_rows = int(input("Enter the number of rows for the diamond pattern: "))
for i in range(num_rows):
        print(' ' * (num_rows - i - 1), end='')
        print('* ' * (i + 1), end='')
        print('* ' * i)

   
for j in range(num_rows - 1):
        print(' ' * (j + 1), end='')
        print('* ' * (num_rows - j - 1), end='')
        print('* ' * (num_rows - j - 2))
