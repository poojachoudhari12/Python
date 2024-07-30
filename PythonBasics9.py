#Functions in python
#to calculate sum
print("\nto calculate sum")
def Cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum

Cal_sum(2,3)

#to print hello
print("\nto print hello")
def print_hello():
    print("Helloo")

output=print_hello()
print(output) 

#to print avg
print("\nto print average:")
def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enetr z:"))
cal_avg(x,y,z)

#1)waf to print length of list
cities=["sangli","kolhapur","Jaysingpur","Jaipur"]
heroes=["thor","krish","shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#print items from list
print("\nprint items from list")
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heroes)



print("Fact fun:")
def fact(n):
    if(fact==0 or fact==1):
        return 1
    return fact(n-1)*n

fact(3)

print("show fun")
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1) 
    print("End")

show(5)

