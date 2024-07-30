#loops for loop
print("\n\n")
num=[1,2,3,4,5,6]
for val in num:
    if(val==4):
        continue
    print(val)
for item in num:
    if(item==4):
        continue
    print(item)
    
print("\n\n")
str="SakshamChoudhari"
for char in str:
    print(char)

#practice Questions
print("\n\nto print elements of list")
#1)to print elements of list
nums=[1,2,3,4,5]
for ele in nums:
    print(ele)

#2)SEARCH FOR ELEMENT IN TUPLE USING FOR LOOP
print("\n\nSEARCH FOR ELEMENT IN TUPLE USING FOR LOOP")
nums=[1,2,3,4,5]
x=int(input("Enter search value:"))
for le in nums:
    if(x==le):
        print("Found")
    

