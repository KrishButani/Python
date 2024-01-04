#1 Create an empty tuple
tup=()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=('krish','rohan','kirtan','utsav')
brothers=('ravi','Krish','Kirtan','mohit')

#3 Join brothers and sisters tuples and assign it to siblings
siblings=brothers + sisters

#4 How many siblings do you have?
print("Sibilings:",len(siblings))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
familymembers=('yash','riya') + siblings
print("\nModified:",familymembers)