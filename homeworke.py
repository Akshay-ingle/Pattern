# Input for the number of rows
rows = int(input("Enter the number of rows: "))

# Generating a mirrored right-angled triangle
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)
