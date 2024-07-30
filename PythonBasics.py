#Variable and data type

#print
print("Hello world")

print("Pooja is my name")
print("My age is 20")

print("Pooja is my name.","My age is 20")
print("Pooja is my name. My age is 20")

print(35)
print(30+20)

#variable 
print("\n\n")
name="pooja"
age=20
price=23.33
print("my name is:",name)
print("my age is:",age)
print("The price is:",price)

#Rules for identifier
print("\n\n")
print("The type of name is:",type(name))
print("The type of age is:",type(age))
print("The type of price is:",type(price))

#Data types

#we can print string
print("\n\nwe can print string")
name1="sk"
name2='sk'
name3='''sk'''
print(name1)
print(name2)
print(name3)

age=20
old=False
a=None
print(type(old))
print(type(a))

#Keywords
#perform arithmatic operation
a=6
b=3
print("\n\nperform arithmatic operation")
print("the value of a is:",a)
print("the value of b is:",b)
diff=a-b
print("the diff is:",diff)
sum=a+b
print("the sum is:",sum)
print("the product is:",a*b)
print("the div is:",a/b)
print("the power is:",a**b)

#Relational Operation
c=50
d=60
print("\n\nRelational operation")
print("the value of c is:",c)
print("the value of d is:",d)
print("Is c and d are equal:",c==d)
print("Is c and d are  not equal:",c!=d)
print("Is c is greater or equal to d:",c>=d)
print("Is c less or equal to d :",c<=d)
print("Is c less d are equal:",c<d)

#logical Operation
e=50
f=100
print("\n\nlogical Operation")
print("the value of e is:",e)
print("the value of f is:",f)
print("not True:",not True)
print("Is e greter than f:",e>f)
print("not (e>f):",not (e>f))
val1=True
val2=True
print("the value of val1 is:",val1)
print("the value of val2 is:",val2)
print("and Operation on val1 and val2:",val1 and val2)
print("or Operation on val1 and val2:",val1 or val2)


                  
#type conversion-->1)Implicit
#               -->2)Explicit
x=10
y=20.24
print("\n\ntype conversion-->1)Implicit")
print("x is:",x)
print("y is:",y)
print("x is of type:",type(x))
print("y is of type:",type(y))
z=x+y
print("print the sum that is z:",z)
print("type of z:",type(z))

#type casting

p=float("22")
q=3.23
print("\n\ntype casting")
print("the value of p is:",p)
print("the value of q is:",q)
print("Type of p become:",type(p))
print("the sum is:",p+q)
r=3.14
print("the value of r:",r)
print("the type of r is:",type(r))
r=str(r)
print("the type of r is after conversion:",type(r))


