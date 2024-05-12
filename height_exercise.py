height = int(input("Enter the height of the triangle: "))

# Loop through each row
for i in range(1, height + 1):
    # Print '*' for each column in the current row
    for j in range(i):
        print("*", end="")
    # Move to the next line after printing the row
    print()