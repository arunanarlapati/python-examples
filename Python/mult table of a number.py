# Python program to print the multiplication table of a number up to 10
# Function to print the multiplication table of a number up to 10
def printTable(num):
    for i in range(1, 11):
        print(num, "*", i, " =", num*i)

# Driver Code
num = int(input("enter any number:"))
print("Number:", num)
print("Multiplication table of", num)
printTable(num)