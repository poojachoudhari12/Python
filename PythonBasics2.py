# String and Data types
str="this is string.\nwe are creating it in python"
print(str)
#concatination of strings
str1="Pooja"
str2="Choudhari"
print("str1:",str1)
print("str2:",str2)
print("The concatination of str1 and str2",str1+str2)
print("the len of str1:",len(str1))
print("the len of str2:",len(str2))
Final_str=str1+" "+str2
print(Final_str)
print("THe length of Final_str",len(Final_str))

#indexing
print("\n\nIndexing")
str3="Sohan Choudhari"
print(str3)
print("str3[0]:",str3[0])
print("str3[5]:",str3[5])
print("str3[6]:",str3[6])
print("str[len(str3)-1]:",str3[len(str3)-1])
#str3[4]="@"
#print(str3)

#indices
print("\n\nIndices")
print("str3[:4]",str3[:4])
print("str3[0:]",str3[0:])
print("str3[4:7]",str3[4:7])
print("str3[5:len(str3)]",str3[5:len(str3)])
print("str3[-5:-1]",str3[-5:-1])
print("str3[-5:0]",str3[-5:0])

#string function
print("\n\nstring function")
str4="i am studing Python from begginning"
print(str4)
print(str4.endswith("ss"))
print(str4.capitalize())
print(str4.replace("python","Java"))
print("finding string studing :",str4.find("studing"))
print("fing string pooja:",str4.find("pooja"))
print("finding count of a:",str4.count("a"))

#Conditional statement
print("\n\nConditional statement")
light="Green"
print("Light:",light)
if(light=="Red"):
    print("Stop")
elif(light=="Green"):
    print("go")
elif(light=="Yellow"):
    print("Wait")

#prg to implement to grade
print("\n\nprg to implement to grade")
marks=int(input("Enter marks:"))
print("Marks:",marks)
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C" 
elif(marks>=60 and marks<70):
    grade="C"      
elif(marks>=50 and marks<60):
    grade="D"
else:
    grade="E"
print("Grades of student is:->",grade)


##Practice Quetions
#1)WAP to check if a no. entered is odd or even
print("\n\nto check if a no. entered is odd or even")
num=int(input("Enter a no:"))
if(num%2==0):
    print("Even no.")
else:
    print("Odd no.")

#to find greater no. among three no.
print("\n\nto find greater no. among three no.")
a=int(input("Enter 1st no.:"))
print("1st no.:",a)
b=int(input("Enter 2nd no.:"))
print("2nd no.:",b)
c=int(input("Enter 3rd no.:"))
print("3rd no.:",c)
if(a>=b and a>=c):
    print("a is greater no.")
elif(b>=c):
    print("b is greater")
else:
    print("c is greater")      

          