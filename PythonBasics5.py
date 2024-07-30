#Sets in python
print("\nSets in python")
collection={2,3,1,2,3,2,1,6}
print("collection={2,3,1,2,3,2,1,6}")
print(collection)
print("len(collection):",len(collection))
print("type(collection):",type(collection))
collection.add(99)
collection.add(11)
print(collection)
collection.remove(2)
print(collection)
collection.clear()
collection1={2,3,4,6,78,9}
print("collection1={2,3,4,6,78,9}")
print(collection)
print("\nUnion operations")
print("collection.union(collection1):",collection.union(collection1))
print("collection.intersection(collection1):",collection.intersection(collection1))
print(collection)
print(collection1)


#practice questions
#1)
dictionary={
    "table":["a piace of furniture","list of facts and figure"],
    "cat":"a small animal"
}
print(dictionary)

#2)
marks={}
x=int(input("enter phy marks:"))
marks.update({"phy":x})
x=int(input("enter math marks:"))
marks.update({"math":x})
x=int(input("enter chem marks:"))
marks.update({"chem":x})
print(marks)

#3)
values={9,9.0}
values1={9,"9.0"}
values2={
    ("float",9.0),("int",9)
}
print("\n\n")
print(values)
print(values1)
print(values2)
