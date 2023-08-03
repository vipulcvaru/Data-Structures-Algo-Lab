# Function to perform the partition step of Quick Sort
def partition(list1, start, end):
    pivot = list1[start]  # Select the first element as the pivot
    left = start + 1  # Pointer to move from left to right
    right = end  # Pointer to move from right to left

    while True:
        # Move the left pointer to the right until a value greater than the pivot is found
        while left <= right and list1[left] <= pivot:
            left += 1

        # Move the right pointer to the left until a value smaller than the pivot is found
        while left <= right and list1[right] >= pivot:
            right -= 1

        if left <= right:
            # Swap the elements at left and right pointers to arrange elements around the pivot
            list1[left], list1[right] = list1[right], list1[left]
        else:
            # Break the loop when the pointers cross each other
            break

    # Move the pivot to its correct position in the sorted list
    list1[start], list1[right] = list1[right], list1[start]

    return right  # Return the index of the pivot after partitioning


# Function to perform Quick Sort recursively
def quickSort(list1, start, end):
    if start < end:
        # Perform partition and get the index of the pivot
        part = partition(list1, start, end)

        # Recursively sort the elements before and after the pivot
        quickSort(list1, start, part - 1)
        quickSort(list1, part + 1, end)

    return list1


# Get the number of students and their percentages from the user
list1 = []
n = int(input("Enter number of students: "))
for i in range(n):
    list1.append(float(input(f"Enter the percentage of student{i+1}: ")))

# Print the original unsorted list
print("Array Before Quick Sorting:")
print(list1)

# Sort the list using Quick Sort and print the sorted list
print("Array After Quick Sorting:")
print(quickSort(list1, 0, n - 1))

# Check and print the top five scores if there are at least five students
if n < 5:
    print("Can't Print Top Five Scores as Length of array is less than 5")
elif n == 5:
    print("Top Five Scores:")
    print(list1)
else:
    print("Top Five Scores:")
    print(list1[n - 5:])
