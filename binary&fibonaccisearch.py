# Binary Search Function
def binary_search(list1, key):
    # Initialize the first and last pointers for binary search
    first = 0
    last = len(list1) - 1
    
    # Perform binary search until the search space is valid (first <= last)
    while first <= last:
        # Calculate the middle index
        mid = (first + last) // 2
        
        # Check if the middle element is the target element
        if list1[mid] == key:
            return mid
        # If the target is greater than the middle element, search the right half
        elif key > list1[mid]:
            first = mid + 1
        # If the target is smaller than the middle element, search the left half
        else:
            last = mid - 1
    
    # If the element is not found, return -1
    return -1

# Fibonacci Search Function....
def fibonacci_search(a, target):
    n = len(a)
    fi_2 = 0
    fi_1 = 1
    fibn = fi_1 + fi_2
    
    # Calculate the Fibonacci number that is greater than or equal to the length of the list
    while fibn <= n:
        fi_2 = fi_1
        fi_1 = fibn
        fibn = fi_1 + fi_2

    offset = -1
    # Perform Fibonacci search until the current Fibonacci number is zero
    while fi_1 != 0:
        # Calculate the index to be checked
        i = min((offset + fi_2), n - 1)
        
        # Compare the target element with the current element at index i
        if target > a[i]:
            # If the target is greater, reduce the search range by moving Fibonacci indices backward
            fibn = fi_1
            fi_1 = fi_2
            fi_2 = fibn - fi_1
            offset = i
        elif target < a[i]:
            # If the target is smaller, reduce the search range by moving Fibonacci indices backward
            fibn = fi_2
            fi_1 = fi_1 - fi_2
            fi_2 = fibn - fi_1
        elif target == a[i]:
            # If the target is found, return the index where it is located
            return i
    
    # If the element is not found, return -1
    return -1

# Create a dynamic list based on user input
list1 = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    num = int(input(f"Enter element {i+1}: "))
    list1.append(num)

# Perform binary search on the dynamic list
key = int(input("Enter the element to search using binary search: "))
index = binary_search(list1, key)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the list using binary search.")

# Perform Fibonacci search on the dynamic list
target = int(input("\nEnter the element to search using Fibonacci search: "))
index2 = fibonacci_search(list1, target)

if index2 != -1:
    print("Element found at index", index2, "using Fibonacci search")
else:
    print("Element not found in the list using Fibonacci search.")
