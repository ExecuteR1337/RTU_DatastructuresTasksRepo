def hello_name():
    while True:
        name = input("Type your name: ")
        print(f"Hello {name}!")

def odd_or_even():
    while True:
        try: number = int(input("Type the number to check: "))
        except ValueError: 
            print("Input the number!")
            return
        if number%2 == 0: print("The number is even!")
        else: print("The number is odd!")

def calculator():
    while True:
        user_input = input("\nPlease type 2 operands separated by a comma (e.g. 2,3) for floating point use a dot (e.g. 2.5,3.5): ")
        try: input1, input2 = map(float, user_input.split(','))
        except ValueError:
            print("Read the instructions!")
            return
        print("\n1 - '+'\n2 - '-'\n3 - '*'\n4 - '/'")
        try: operation = int(input("Pick the operation by typing number: "))
        except ValueError:
            print("Bruh...")
            return
        if operation == 1: print("Result: ", input1 + input2)
        elif operation == 2: print("Result: ", input1 - input2)
        elif operation == 3: print("Result: ", input1 * input2)
        elif operation == 4:
            if input2 == 0: print("Cannot divide by zero!")
            else: print("Result: ", input1 / input2)
        else: print("Bruh...")

def factorial():
    while True:
        try: number = int(input("\nType the number to calculate its factorial: "))
        except ValueError:
            print("\nBruh...\n")
            return
        factorial=1
        for i in range(1, number+1):
            factorial*=i
        print("\nResult:", factorial)

def prime_or_not():
     while True:
        try: number = int(input("\nType the number to find out if it is prime: "))
        except ValueError:
            print("\nBruh...\n")
            continue
        if number < 2:
            print(f"\nThe number {number} is not prime!")
            continue
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(f"\nThe number {number} is not prime!")
                is_prime = False
                break
        if is_prime: print(f"\nThe number {number} is prime!")



# hello_name()
# odd_or_even()
# calculator()
# factorial()
prime_or_not()