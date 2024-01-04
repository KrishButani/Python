#1 Unpack siblings and parents from family_members
familymembers=('Vaibhav', 'Nehil', 'Kunj', 'Krish', 'Kirtan', 'Sahil', 'Stuti', 'Mohit', 'Kiara', 'Dhruvi')
father,mother,*siblings=familymembers
print("Father:"+father+"\nMother:"+mother+"\nSibllings:"+str(siblings))

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Apple','Mango','Grapes','Kiwi')
vegetables=('Tomato','Potato','Pumpkin','Carrot')
animal_products=('Milk','Grass','Meat')
food_stuff_tp=fruits + vegetables + animal_products
print("\n",food_stuff_tp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stufflist=list(food_stuff_tp)
print("\nList:",food_stufflist)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("\nMiddle item from tuple:",food_stuff_tp[len(food_stuff_tp)//2])
print("Middle item from list:",food_stufflist[len(food_stufflist)//2])

#5 Slice out the first three items and the last three items from food_staff_lt list
print("\nFirst three items:",food_stufflist[:3])
print("Last three items:",food_stufflist[-3:])

#6 Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp) ----NO execution further as tuple delted


#7 Check if an item exists in tuple:
#print('Meat' in food_stuff_tp) ----False bcs tuple deleted

#8 Check if 'Estonia' is a nordic country
nordiccountries=('Denmark','Finland','Iceland','Norway','Sweden')
print("\nIs Estonia a Nordic country:",'Estonia' in nordiccountries)

#9 Check if 'Iceland' is a nordic country
print("\nIs Iceland a Nordic country:",'Iceland' in nordiccountries)

# py nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')