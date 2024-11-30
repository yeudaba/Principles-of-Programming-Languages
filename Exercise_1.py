

#יוצרים מערך של מספרים שלמים

"""אנחנו קולטים כל פעם מספר ובודקים האם הוא מספר שלם וחיובי
במידה וכן אני מוסיף אותו למערך במידה והוא אות או מספר אי חיובי אני זורק חריגה
 ומדפיס את הערך שנוצר"""


def IntegerNumber():
    arr = []
    while True:
        try:
            number = int(input("Please enter an integer: "))
            if number > 0:
                arr.append(number)
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            break
    return arr


#print(IntegerNumber())




"""יצירת מערך שכל הספרות שלו מופיעות מספר הפעמים במערך השני"""
def Array1(arrA,arrB):# [3,2,2]
    NewArray = []
    index = 0
    for i in arrB:
        while i >0:
            NewArray.append(arrA[index])
            i -=1
        index +=1
    return NewArray

A = [6,7,8]
B = [2,1,3]

#print(Array1(A,B))



empty_tuple = ()
one_sized = (66.13, )
ranged = tuple(range(2, 4))
joined = one_sized + ranged

#print(joined)

x,y,z=3,4,5

#print(z)

x = [1,2,3]

a,b,c=x

f=lambda a,b: (a+b) # קיצור דרך במקום ליצור פונקציה שתעשה פעולה

res1= f(a,b)

print(res1)