# chaos program REDUX

global x
global y
global n

# Get values from user
print()
n = eval(input("How many times? "))
x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

# Run the numbers
def run():
    global x
    global y
    global n

    for i in range(n):
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        print("\t\t", x, "\t\t", y)

# Output
print()
print("input\t\t", x, "\t\t\t", y)
print("-----------------------------------------------------")
run()
print()
