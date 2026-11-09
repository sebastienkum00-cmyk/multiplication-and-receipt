print("WELCOME TO MY PYTHON PROGRAM")

print("1. Multiplication")
print("2. Print a receipt")

choice = input("Choose an option: ")

if choice == "1":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    answer = num1 * num2

    print("The answer is:", answer)

elif choice == "2":
    print("\n========== SHOP RECEIPT ==========")

    serial = input("Enter item serial number: ")
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    total = quantity * price

    print("\n========== RECEIPT ==========")
    print("Serial Number:", serial)
    print("Item Name:", name)
    print("Quantity:", quantity)
    print("Unit Price:", price, "FCFA")
    print("Total:", total, "FCFA")
    print("============================")

else:
    print("Invalid choice. Please select 1 or 2.")
