#Dictionary in python

info={
    "Name":"Daisy Choudhari",
    "Age":20,
    "Is_Adult":True,
    "Subjects":["Python","Java","Cpp"],
    "Topics":("dict","set"),
    "Marks":97.2
}
print(info)
print(info["Name"])
print(info["Topics"])
print(info["Marks"])
info["Name"]="Sia Saxsena"
print(info)
info["Surname"]="Choudhari"
print(info)

#Nested disctionary
print("\n\nNested disctionary")
Student={
    "name":"Saksham Choudhari",
    "Marks":{
        "Maths":23,
        "Science":24,
        "English":23
    }
}
print("Student:",Student)
print('''Student["name"]:''',Student["name"])
print('''Student["Marks"]:''',Student["Marks"])
print('''Student["Marks"]["Science"]:''',Student["Marks"]["Science"])
#Dictionary Methods
print("\n#Dictionary Methods")
print("Student.keys():",Student.keys())
print('''to convert dict to list:''',list(Student.keys()))
print('''List(Student.values()):''',list(Student.values()))
print('''list(Student.items()):''',list(Student.items()))
print('''Student.get("name:"):''',Student.get("name:"))
print(Student.update({"name":"Pooja choudhari"}))
print(Student)

print("\n\n")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)