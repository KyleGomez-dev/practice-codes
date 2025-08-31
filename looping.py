#make a nested for loop that will print a pyramid of stars with the number of rows input by the user.
rows = int(input("Enter the number of rows for the pyramid: "))
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()



