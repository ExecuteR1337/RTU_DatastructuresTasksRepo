def init():
    array_str = input("\nPlease type in coma-separated array (e.g. 1,2,3,4,5) for floating point use dot (e.g. 2.5,3.5): ")
    try:
        array = list(map(float, array_str.split(',')))
    except ValueError:
        print(f"\nValue Error, please input the numbers:\n")
        return
    print("\n1 - Find Sum\n2 - Find Largest\n3 - Reverse\n4 - Count Occurrences\n5 - Merge 2 Arrays\n")
    try:
        choice = input("Please choose desired operation: ")
    except ValueError:
        print(f"\nValue Error, please input the numbers!\n")
        return

############################################################

    if choice == "1":
        print(f"\nSum: {sum(array)}\n")
        init()
    elif choice == "2":
        print(f"\nLargest Member: {max(array)}\n")
        init()
    elif choice == "3": array_reverse(array)
    elif choice == "4": occurrences_counter(array)
    elif choice == "5": merge_arrays(array)
    else: 
        print("Please pick from 1 to 5!\n")
        init()
        
############################################################

def array_reverse(array):
    reversed_array = array[::-1]
    print("Reversed Array: ", reversed_array)
    init()

def occurrences_counter(array):
    try:
        target = float(input("\nType the member to search: "))
    except ValueError:
        print(f"\nValue Error, please input the numbers:\n")
        return
    occurrences = array.count(target)
    print(f"\nNumber of Occurrences of {target} is: ", occurrences)
    init()

def merge_arrays(array1):
    array2_str = input("\nPlease type second coma-separated array: ")
    try:
        array2 = list(map(float, array2_str.split(',')))
    except ValueError:
        print(f"\nValue Error, please input the numbers:\n")
        return
    merged_array = array1+array2
    print("\n Merged Array: ", merged_array)
    init()

init()