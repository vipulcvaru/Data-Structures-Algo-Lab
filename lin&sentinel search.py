# Function for linear search algorithm
def linear_search(list1, key):
    for i in range(len(list1)):
        if list1[i] == key:
            return i
    return -1

# Function for sentinel search algorithm
def sentinel_search(list1, key):
    last = list1[-1]
    list1[-1] = key
    i = 0
    while list1[i] != key:
        i = i + 1

    if i != len(list1) - 1:
        return i

    if last == key:
        return len(list1) - 1

    return -1

# Get the list of students from the user
while True:
    stud_list_input = input("Enter the list of student's ID (separated by spaces): ")
    stud_list = stud_list_input.split()
    # Check if all elements can be converted to integers
    if all(item.isdigit() for item in stud_list):
        stud_list = [int(num) for num in stud_list]
        break
    else:
        print("Invalid input. Please enter a list of integers.")

# Get the key to search for from the user
while True:
    key_to_search_input = input("Enter the student ID to search for: ")
    # Check if the key can be converted to an integer
    if key_to_search_input.isdigit():
        key_to_search = int(key_to_search_input)
        break
    else:
        print("Invalid input. Please enter a valid integer for the student ID.")

# Perform linear search
index1 = linear_search(stud_list, key_to_search)
if index1 == -1:
    print("Student not found !! \n")
else:
    print("Student found at index:", index1)

# Perform sentinel search
index2 = sentinel_search(stud_list, key_to_search)
if index2 == -1:
    print("Student not found !! \n", index2)
else:
    print("Student present at index:", index2)
