# Function to perform Bubble Sort
def bubble_sort(list1):
    n = len(list1)
    for i in range(n - 1):  # Outer loop for the number of passes (n-1 passes required for n elements)
        for j in range(0, n - i - 1):  # Inner loop for each pass, reduces range since largest elements are already sorted
            if list1[j] > list1[j + 1]:  # Compare adjacent elements
                # Swap the elements to bring the larger one to the right
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp

# Function to perform Selection Sort
def selection_sort(list1):
    n = len(list1)
    for i in range(n - 1):  # Outer loop for the number of passes (n-1 passes required for n elements)
        for j in range(i + 1, n):  # Inner loop to find the minimum element from the unsorted part of the list
            if list1[i] > list1[j]:  # Compare the current element with the next element
                # Swap the elements to bring the smaller one to the left
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp

# Function to get student percentages as input
def get_student_percentages():
    n1 = int(input("Enter number of students in the class: "))
    print("Enter students' percentages:")
    # Create a list to store student percentages using list comprehension
    list1 = [float(input(f"Enter percentage of student {i+1}: ")) for i in range(n1)]
    return list1

# Function to print a list with a label
def print_list(label, list1):
    print(label)
    print(list1)

# Main code
# Get student percentages from the user
percentages_list = get_student_percentages()
print_list("List before sorting:", percentages_list)

# Sorting using Bubble Sort
# Make a copy of the original list to avoid modifying it during sorting
bubble_sorted_list = percentages_list.copy()
bubble_sort(bubble_sorted_list)
print_list("Sorted array using Bubble Sort:", bubble_sorted_list)

# Sorting using Selection Sort
# Make a copy of the original list to avoid modifying it during sorting
selection_sorted_list = percentages_list.copy()
selection_sort(selection_sorted_list)
print_list("List after Selection Sort:", selection_sorted_list)
