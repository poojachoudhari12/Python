#range function
print("\n\nrange function")
for i in range(11):
    print(i)

print("\n")
for i in range(1,21):
    print(i)

print("\n")
for i in range(1,21,2):
    print(i)

#practice Questions
#to print from 10 to 1
print("\nto print from 10 to 1")
for i in range(10,0,-1):
    print(i)

print("\nto print the multiplication table:")
n=int(input("Enter a no:"))
for i in range(1,11):
    print(n*i)
    
#pass statemant in Python
print("\npass statemant in Python")
for i in range(5):
    pass
print("some useful work")

#practice questions:
#1)to print the sum of numbers
sum=0
n=7
for i in range(0,n+1):
    sum=sum+i
print("\nSum:",sum)    

#2)to find factorial of n numbers
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial:",fact) 