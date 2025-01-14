import string
from functools import reduce
from currency import currency

#1
def Course_Grade(student1):
    """
        Filters students based on their course grades.

        Parameters:
        student1 (tuple): A tuple containing (student_name, course, grade).

        Returns:
        str: The student name followed by ", " if the grade > 90 and course in ["Math", "Science", "History"].
        """
    student_name,course,grade = student1
    if grade > 90 and course in ["Math","Science","History"]:
        return student_name+", "



grades = [("Alice","Math",95),("Alice","Science",92),("Alice","History",88),("Bob","Math",93),("Bob","Science",91),("Bob","History",90),("Charlie","Math",89)]

Student_Grade =list(filter(Course_Grade ,grades))

studentName=list(map(lambda x: x[0],Student_Grade))

NumberStudent = list(set(studentName))

##################################################
#################################################

#2
def is_prime_recursive(n, x=None):
    """
       Checks if a number is prime using recursion.

       Parameters:
       n (int): The number to check.
       x (int, optional): The divisor to check divisibility. Defaults to None (start from n-1).

       Returns:
       bool: True if the number is prime, False otherwise.
       """
    if n <= 1:
        return False
    if x is None:
        x = n - 1
    if x == 1:
        return True
    if n % x == 0:
        return False
    return is_prime_recursive(n, x - 1)


numbers1 = [2,3,4,5,6,7,8,9]

Numbers=(list(filter(is_prime_recursive,numbers1)))

a2 = list(map(lambda x: x*x,Numbers))
##################################################
#################################################

#3

products = [ ("Laptop", "electronics", 1200),
             ("Table", "furniture", 300),
             ("Chair", "furniture", 150),
             ("Phone", "electronics", 700),
             ("Pen", "stationery", 5)]

electronics = list(filter(lambda p: p[1] == "electronics", products))
furniture = list(filter(lambda p: p[1] == "furniture", products))
stationery = list(filter(lambda p: p[1] == "stationery", products))

most_electronics = max(electronics, key=lambda p: p[2])
most_furniture = max(furniture, key=lambda p: p[2])
most_stationery = max(stationery, key=lambda p: p[2])

A = []
A.append(most_electronics)
A.append(most_furniture)
A.append(most_stationery)

##############################################
#############################################

#4

numbers = [1,2,3,4,5,6,10,15]

Num1=list(filter(lambda x: x % 5==0 or x % 3 ==0,numbers))
Num2 = reduce(lambda x, y: x * y, Num1)


################################################
################################################

text = "Python, programming: is fun! Enjoy coding."

text = text.split()
text1 = [word.strip(string.punctuation) for word in text]

string1= list(filter(lambda x: len(x)>7,text1))

#################################################
#################################################

def make_mutable_rlist(elements1=None):
    """
       Creates a mutable recursive list with various operations.

       Parameters:
       elements1 (list, optional): Initial elements to populate the list. Defaults to None.

       Returns:
       function: A dispatch function to perform operations on the list.
       """
    rlist = [] if elements1 is None else elements1[:]

    def D(message):
        """
               Dispatches operations on the mutable list based on the message.

               Parameters:
               message (str): The operation to perform (e.g., 'push_first', 'pop_first', 'str', etc.).

               Returns:
               function: The corresponding operation function.
               """
        if message == 'push_first':
            def push_first(value):
                """
                               Adds a value to the beginning of the list.

                               Parameters:
                               value: The value to add.
                               """
                rlist.insert(0, value)
            return push_first

        elif message == 'pop_first':
            def pop_first():
                """
                               Removes and returns the first element of the list.

                               Returns:
                               The first element of the list.

                               Raises:
                               IndexError: If the list is empty.
                               """
                if not rlist:
                    raise IndexError("pop from empty list")
                return rlist.pop(0)
            return pop_first

        elif message == 'str':
            def to_string():
                """
                              Returns a string representation of the list.

                              Returns:
                              str: A string representing the list.
                              """
                return str(rlist)
            return to_string

        elif message == 'slice':
            def slice_list(start, end):
                """
                               Returns a new mutable list containing elements from the specified slice.

                               Parameters:
                               start (int): The starting index (inclusive).
                               end (int): The ending index (exclusive).

                               Returns:
                               function: A new mutable list containing the sliced elements.
                               """
                elements = rlist[start:end]
                return make_mutable_rlist(elements)
            return slice_list

        elif message == 'extend':
            def extend_list(other_mutable_list):
                """
                                Extends the list with elements from another mutable list.

                                Parameters:
                                other_mutable_list (function): Another mutable list to extend from.
                                """
                iterator = other_mutable_list('get_iterator')()
                while iterator('hasNext')():
                    rlist.append(iterator('next')())
            return extend_list

        elif message == 'copy_constructor':

            def copy_constructor():
                """
                                Creates a copy of the mutable list.

                                Returns:
                                function: A new mutable list containing the same elements.
                                """
                return make_mutable_rlist(rlist)
            return copy_constructor

        elif message == 'get_iterator':
            def get_iterator():
                """
                                Returns an iterator for the list.

                                Returns:
                                function: A dispatch function for the iterator.
                                """
                Index = [0]

                def iterator_dispatch(it_message):
                    """
                                        Dispatches operations on the iterator.

                                        Parameters:
                                        it_message (str): The operation to perform ('hasNext', 'next').

                                        Returns:
                                        function: The corresponding iterator operation.
                                        """
                    if it_message == 'hasNext':
                        return lambda: Index[0] < len(rlist)
                    elif it_message == 'next':
                        def next_item():
                            """
                                                        Returns the next item in the iterator.

                                                        Returns:
                                                        The next item in the list.

                                                        Raises:
                                                        StopIteration: If there are no more elements.
                                                        """
                            if Index[0] >= len(rlist):
                                raise StopIteration("No more elements")
                            item = rlist[Index[0]]
                            Index[0] += 1
                            return item
                        return next_item
                    else:
                        raise ValueError("Invalid iterator message")
                return iterator_dispatch
            return get_iterator

        else:
            raise ValueError("Invalid message")

    return D

#####################################################
#####################################################

if __name__ == "__main__":
    print("Question 1:")
    print(NumberStudent)

    print("Question 2:")
    print(a2)

    print("Question 3:")
    print(A)
    print("Question 4:")
    print(Num2)
    print("Question 5:")
    print(string1)
    print("\n")
    print("Part 2:")
    print("Question 1: ")
    c = currency.make_currency(10.50, '$')
    print(c('get_value')('amount'))
    print(c('get_value')('symbol'))
    c('set_value')('amount', 50)
    print(c('get_value')('amount'))
    print(c('str'))
    c('convert')(lambda x: x * 3.87, '₪')
    print(c('str'))

    print("Question 2: ")
    my_list = make_mutable_rlist()
    for x in range(4):
        my_list('push_first')(x)
    print(my_list('str')())
    ext = my_list('copy_constructor')()
    my_list('extend')(ext)
    print(my_list('str')())
    sliced = my_list('slice')(0, 2)
    print(sliced('str')())
    your_list = my_list('copy_constructor')()
    print(your_list('str')())
    it = my_list('get_iterator')()
    while it('hasNext')():
        print(it('next')())

