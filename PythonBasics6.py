##Looping concept in python
print("\n\nLooping concept in python")
count=0
while count<=5:
    print("Hello",count)
    count+=1

#1)to print from 1 to 10
print("\n\nto print from 1 to 10")
i=1
while i<=10:
    print(i)
    i+=1
print("Done")

#2)to print from 10 to 1
print("\n\nto print from 10 to 1")
i=10
while i>=1:
    print(i)
    i-=1
print("Done")

#3)to print table of any no.
print("\n\nto print table of any no.")
N=int(input("Enter no.:"))
i=1
while i<=10:
    print(N*i)
    i+=1

#4)print the list using loop
print("\n\nprint the list using loop")
elements=[2,11,4,33,7,12,5]
i=0
length=len(elements)
print("length:",length)
while i<=length-1:
    print(elements[i])
    i=i+1

#5)to search for element
print("\n\nto search for element")
x=int(input("Enter the search:"))
i=0
while i<=length-1:
    if(x==elements[i]):
        print("found")
    else:
        print("not found")   
        
    i=i+1






