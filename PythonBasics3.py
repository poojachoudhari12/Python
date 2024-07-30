#list and Tuple 
print("#list and Tuple ")
print("\nList example")
marks=[2,23,24,13,22,25]
print("Marks:",marks)
print("marks[0]:",marks[0])
print("marks[4]:",marks[4])
#print("marks[len(marks)]:",marks[len(marks)])

#slicing
print("\nslicing")
print("marks[0:3]:",marks[0:3])
print("marks[:3]:",marks[:3])
print("marks[0:5]:",marks[0:5])
print("marks[1:6]:",marks[1:6])
#List methods
print("\nList methods")
print("marks.append(99):",marks.append(99))
print(marks)
print("marks.sort():",marks.sort())
print(marks)
print("marks.sort(decresing order):",marks.sort(reverse=True))
print(marks)
print("marks.reverse():",marks.reverse())
print(marks)
print("marks.insert(idx,ele):",marks.insert(1,100))
print(marks)

print("\n\n")
student=['Pooja',89,"Delhi"]
print("Student:",student)
student[0]="Komal"
print("Student:",student)

#tuple example
print("\nTuple example")
Rno=(2,23,24,13,22,25)
print("Roll no:",Rno)
print("Rno[0]:",Rno[0])
print("Rno[4]:",Rno[4])
print("Rno.index(24):",Rno.index(24))
print("Rno.count(24):",Rno.count(24))

#Practice questions
#1)wap to enter 3 movies name and store in list
print("\n\nto enter 3 movies name and store in list")
movies=[]
movies.append(input("Enter 1st movie name:"))
movies.append(input("Enter 2nd movie name:"))
movies.append(input("Enter 3rd movie name:"))
print(movies)

#2)to check if list contain palindrome  of elements
list1=['m','a','a','m']
print("\n\nto check if list contain palindrome  of elements")
print(list1)
copy_list1=list1.copy()
copy_list2=copy_list1.reverse()
if(copy_list2==list1):
    print("palindrome")
else:
    print("Not palindrome")    

#3)to count no. of student got A grade in tuple and sort grades
Grade=("A","B","E","A","A")
print("\n\nto count no. of student got A grade in tuple and sort grades")
print(Grade)

Grade=["A","B","E","A","A"]
print("The no. of student got A grade are:",Grade.count("A"))
Grade.sort()
print(Grade)