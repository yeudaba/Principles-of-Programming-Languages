# yeuda

print("Question 1")
def binary_search(arr, num, S1, end):
    """
    A recursive function that performs a binary search.

    Parameters:
    arr (list): A sorted list to search through.
    target (int): The value to search for.
    start (int): The starting index of the search range.
    end (int): The ending index of the search range.

    Returns:
    int: The index where the target value is found, or -1 if the value is not present.
    """
    # Base case: If the range is invalid
    if S1 > end:
        return -1

    # Calculate the middle index
    mid = (S1 + end) // 2

    # Check if the target is at the middle index
    if arr[mid] == num:
        return mid

    # If the target is smaller than the middle element, search the left half
    elif num < arr[mid]:
        return binary_search(arr, num, S1, mid - 1)

    # If the target is larger than the middle element, search the right half
    else:
        return binary_search(arr, num, mid + 1, end)

# Example usage
size=input("Enter the size of the array: ")
arr = []
for i in range(int(size)):
    num6 = int(input("Enter your number for array: "))
    arr.append(num6)
index_start = int(input("Enter the starting index"))
index_end = int(input("Enter the ending index"))

num = int(input("Enter the number to search for: "))
print(binary_search(arr, num, index_start, index_end))  # Output: 3

print()

##################################################################################################################################################
##################################################################################################################################################
print("Question 2")

size2=input("Enter the size of the array: ")
arr2 = []
for i in range(int(size2)):
    num11 = int(input("Enter your number for array: "))
    arr2.append(num11)

New_number2 = int(input("Enter the number to search for: "))
def generate_combinations(arr2, New_number):# [1,2,3,4]  New_number=4
    """
       Generates all possible combinations of New_number elements from the given list.

       Parameters:
       lst (list): The list of elements to choose from.
       New_number (int): The number of elements in each combination.

       Returns:
       list of lists: A list containing all possible combinations of New_number elements.
       """
    # Base case: If New_number is 0, there is exactly one combination - an empty list
    if New_number == 0:
        return [[]]

    if not arr2 or New_number > len(arr2):
        return []

    first = generate_combinations(arr2[1:], New_number - 1)
    first = [[arr2[0]] + combination for combination in first]

    without_number = generate_combinations(arr2[1:], New_number)
    return first + without_number


print(generate_combinations(arr2, New_number2))

print()
##################################################################################################################################################
##################################################################################################################################################

print("Question 3")
x = 5

# Define a lambda function to multiply a number by 2
f = lambda x: x * 2  # Multiply the input by 2
def apply_twice(f, x):
    """
        Applies the given function `f` to the input `x` twice and returns the sum of the results.

        Args:
            f (function): A function that takes one argument and returns a value.
            x (int): The input value to which the function will be applied.

        Returns:
            int: The sum of applying the function `f` twice to the input `x`.

        Example:
             f = lambda x: x * 2
            apply_twice(f, 3)
            12
        """
    sum = 0 # Initialize the sum to zero
    for i in range(2):
        # Add the result of applying the function `f` to `x` to the sum
        sum = sum + f(x)# 1. sum = 0 + 6;    2. sum= 6+6;

    return sum

print(apply_twice(f,x))
print()


print("Question 4")

def create_multiplier(n):
    """
      Creates a multiplier function that multiplies any given number by n.

      Args:
          n (int): The number to multiply by.

      Returns:
          function: A function that takes an input x and returns x multiplied by n.

      """
    return lambda x: x * n# n=2

multiplier_by_3 = create_multiplier(3)
print(multiplier_by_3(10))


