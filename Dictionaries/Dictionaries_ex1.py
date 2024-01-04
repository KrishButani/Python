#1 Create an empty dictionary called dog
dog = {}


#2 Add name, color, breed, legs, age to the dog dictionary
Dog = {
     'Name': 'Spike',
    'Color': 'Black',
    'Breed': 'German Shepherd',
     'Legs': 4,
      'Age': 2
}
for Tittle , Details in Dog.items():
    print(f"{Tittle.title()} : {Details}")


#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Student = {
    'First_Name': 'Krish',
     'Last_Name': 'Butani',
        'Gender': 'Male',
           'Age': 19,
'Marital Status': "Un-Married",
        'Skills': ['C & C++','Java', 'Communication', 'MERN-Stack'],
       'Country': 'India',
          'City': 'Anand',
       'Address': 'Changa'
}


#4 Get the length of the student dictionary
print(len(Student))


#5 Get the value of skills and check the data type, it should be a list
print(type(Student['Skills']))


#6 Modify the skills values by adding one or two skills
Student['Skills'].append('Esports')
for a in Student['Skills']:
    print(a)


#7 Get the dictionary keys as a list
print(Student.keys())


#8 Get the dictionary values as a list
print(Student.values())


#9 Change the dictionary to a list of tuples using items() method
Stu_Tuple = Student.items()
print(Stu_Tuple)


#10 Delete one of the items in the dictionary
Student.pop('Marital Status')
for Tittle, Details in Student.items():
    print(f"{Tittle.title()} : {Details}")



#11 Delete one of the dictionaries
del Student
# print(Student) --> Gives Variable not defined coz' in LOC 66 we deleted the Student