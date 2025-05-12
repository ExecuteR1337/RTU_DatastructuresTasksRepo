def queue_in_clinic():
    stack = []
    current = 0
    while True:
        new_patient = input('Type the name of new patient or to finish inputing type "0": ')
        if new_patient == "0":
            print(f"-----------------------------------------------------------\nFirst patient in the queue: {stack[current]}")
            next_patient(current)
        else: stack.append(new_patient)
        def next_patient(current):
            decision = input('\nOK. The doctor helped the patient, to call next patient type "0": ')
            if decision == "0":
                current += 1
                try: print(f"-----------------------------------------------------------\nCurrent patient in the queue: {stack[current]}")
                except IndexError: 
                    print("\nNo patients left!\n")
                    return
                next_patient(current)
            else: return

############################################################################################################################################

def string_reverse():
    while True:
        input_text = input('Type something: ')
        try: 
            stack = list(input_text)
            reverser(stack)
        except Exception as e: 
            print(f"Bruh... {e}")
            return  
def reverser(stack):
    stack_rev = []
    for i in range(len(stack) - 1, -1, -1):
        stack_rev.append(stack[i])
    string_output = ''.join(stack_rev)
    print(string_output)

############################################################################################################################################  
        
def is_balanced():
    while True:
        expression = input("Give something that includes only ')', ']', '}': ")
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in expression:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack.pop() != pairs[char]:
                    print("Not Balanced")
                    return
        print("Balanced" if not stack else "Not Balanced")

############################################################################################################################################

def infix_to_postfix():
    expression = input("Enter infix expression: ")
    stack = []
    output = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    print("Postfix:", ''.join(output))

############################################################################################################################################

def evaluate_postfix():
    expression = input("Enter postfix expression: ").strip()
    stack = []
    try:
        for char in expression:
            if char.isdigit():
                stack.append(int(char))
            elif char in {'+', '-', '*', '/'}:
                if len(stack) < 2:
                    raise ValueError("Insufficient operands in the expression.")
                b = stack.pop()
                a = stack.pop()
                if char == '+': stack.append(a + b)
                elif char == '-': stack.append(a - b)
                elif char == '*': stack.append(a * b)
                elif char == '/':
                    if b == 0: raise ZeroDivisionError("Division by zero encountered.")
                    stack.append(a // b)
        if len(stack) != 1: raise ValueError("Invalid postfix expression.")
        print("Evaluation Result:", stack[0])
    except (ValueError, ZeroDivisionError) as e: print("Error:", e)

############################################################################################################################################

# queue_in_clinic()
# string_reverse()
# is_balanced()
# infix_to_postfix()
evaluate_postfix()