#1 Declare an empty list
list1 = list()


#2 Declare a list with more than 5 items
list1=['java','python','mongoDB','react','javascript']


#3 Find the length of your list
# print(len(list1))


#4 Get the first item, the middle item and the last item of the list
first_item = list1[0]
# print(first_item)
middle_item = len(list1)//2
middle_item = list1[middle_item]
# print(middle_item)
last_item = list1[-1]
# print(last_item)


#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = {
    'Name': 'Krish Butani',
    'Age' :19,
    'Height': 6.2,
    'Marital status' :False,
    'Address':'Junagadh'
    }
# print(mixed_data_types)


#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]


#7 Print the list using print()
# print(it_companies)


#8 Print the number of companies in the list
# print(len(it_companies))


#9 Print the first, middle and last company
first_item = it_companies[0]
# print(first_item)
middle_item = len(it_companies)//2
middle_item = it_companies[middle_item]
# print(middle_item)
last_item = it_companies[-1]
# print(last_item)


#10 Print the list after modifying one of the companies
it_companies[0]="TATA"
# print(it_companies)


#11 Add an IT company to it_companies
it_companies.append("IT company")
# print(it_companies)


#12 Insert an IT company in the middle of the companies list
middle_item = len(it_companies)//2
it_companies.insert(middle_item,'IT company')
# print(it_companies)


#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = it_companies[3].upper()
# print(it_companies)


#14 Join the it_companies with a string '#;
Join = '#;'.join(it_companies)
# print(Join)


#15 Check if a certain company exists in the it_companies list.
if "Apple" in it_companies:
    print("Apple Exist in the list")
else:
    print("Apple doesn't Exist in the list")


#16 Sort the list using sort() method
    it_companies.sort()
    

#17 Reverse the list in descending order using reverse() method
    it_companies.reverse()


#18 Slice out the first 3 companies from the list
    print(it_companies[0:2])


#19 Slice out the last 3 companies from the list
    print(it_companies[-3:-1])


# Slice out the middle IT company or companies from the list
if len(it_companies)%2!=0:
    print("\nSlice from middle:",it_companies[len(it_companies)//2])


#21 Remove the first IT company from the list
    print(it_companies.pop(0))


#22 Remove the middle IT company or companies from the list
    print(it_companies.pop(len(it_companies) // 2))


#23 Remove the last IT company from the list
    print(it_companies.pop(-1))


#24 Remove all IT companies from the list
    print(it_companies.clear())


#25 Destroy the IT companies list
del it_companies