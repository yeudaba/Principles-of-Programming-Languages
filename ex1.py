def binary_search(arr, index_Number, num1, num2):
    if num2 == 0:
        return num2
    temp = binary_search(arr, index_Number, num1, num2 - 1)
    if (index_Number == arr[temp]):
        return temp

    else:
        return arr[temp]


arr = [1, 3, 5, 7, 9]
num1 = 7
num2 = 0
num3 = 4

#print(binary_search(arr, num1, num2, num3))

arr1 = [1, 2, 3]

New_number = 2
"""
def generate_combinations(arr1,New_number):
    if(New_number==0):
        return list(arr1[New_number],New_number)
    temp=generate_combinations(,New_number)
    return temp.append(list(arr1[len(arr1),New_number]))

print(generate_combinations(arr1,New_number))

"""


def generate_combinations(arr1, New_number):
    if isinstance(arr1,list) and len(arr1) == 0:
        return list[arr1[0], New_number]
    temp = []
    temp.append(generate_combinations(arr1.pop(-1), New_number))
    if (arr1[len(arr1)] != New_number):
        return temp.append(arr1[New_number-len(arr1)], New_number)
    return temp


#print(generate_combinations(arr1, New_number))

"""
def generate_combinations(arr1, New_number):
    # Base case: if the list is empty, return a new list with the number
    if len(arr1) == 0:
        return [[New_number]]

    # Get the last element and rest of the list
    last_element = arr1[-1]
    rest = arr1[:-1]

    # Recursive call to generate combinations from the rest of the list
    temp = generate_combinations(rest, New_number)

    # Add the new combination with the current last element and New_number
    new_combinations = [comb + [last_element, New_number] for comb in temp]

    return temp + new_combinations

# Example usage
arr1 = [1, 2, 3]
New_number = 4
print(generate_combinations(arr1, New_number))


"""


import Student

student = Student.Student('yeuda','baza')
number = 60


student.__add__(number)
student.__add__(80)
student.__add__(60)

#print(student.Average())

#print(student.sumStudents())

#e= open('Name.txt','w+')

#e.write(' this is my name')

#e.close()


#with open ('Name.txt') as f:

    #for line in f:
        #print(line)


arr = [1,2,3,4,5,6,7,8,9]



def num3(i):
    if i%2 == 0:
        return i





arr1 = list(filter(num3,arr))

print(arr1)