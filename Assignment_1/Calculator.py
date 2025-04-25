def add(x, y):
    return round(x + y, 6)

def subtract(x, y):
    return round(x - y, 6)

def multiply(x, y):
    return round(x * y, 6)

def divide(x, y):
    if y != 0:
        return round(x / y, 6)
    else:
        return "Error: Division by zero"



def calculator():
    print("Simple Calculator")

    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator... Thanks for using me 🧡 Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        else:
            print("❌ Invalid input ❌ Please enter a valid choice (between 1 & 5).")

if __name__ == "__main__":
    calculator()
