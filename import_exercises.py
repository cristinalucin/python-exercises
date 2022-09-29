## 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

# a. Run an interactive python session and import the module. Call the is_vowel function using the . syntax.

is_vowel = fe.is_vowel('a')
print(is_vowel)

## b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip 
## function directly. Call this function with values you choose and print the result.

calculate_tip = fe.calculate_tip(100)
print(calculate_tip)

# c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function
# and give it an alias. Test this function in your notebook.

import function_exercises as fe
letter_grade = fe.get_letter_grade(80)
print(letter_grade)

## 2 Read about and use the itertools module from the python standard library to help you solve the following problems:

#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

list(itertools.product('abc', [1,2,3]))

#How many different combinations are there of 2 letters from "abcd"?

from itertools import combinations
a = combinations('abcd', 2)
len((list(a)))

#How many different permutations are there of 2 letters from "abcd"?

from itertools import permutations
a= permutations('abcd', 2)
len((list(a)))

#3 Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
# Use the load function from the json module to open this file.

import json

json.load(open('profiles.json'))

# Your code should produce a list of dictionaries. Using this data, write some code that calculates and 
# outputs the following information:

# Total number of users
len(profiles)

# Number of active users

counter = 0
for profile in profiles:
    if profile['isActive'] == True:
        counter = counter + 1
print(counter)

# Number of inactive users

counter = 0
for profile in profiles:
    if item['isActive'] == False:
        counter = counter + 1
print(counter)

# Grand total of balances for all users

total_balance = 0
for profile in profiles:
    total_balance += float(profile['balance'].strip('$').replace(',', ''))
print(total_balance)

# Average balance per user

round(total_balance / len(profiles), 2)

# User with the lowest balance

balance_ls = []

for profile in profiles:
    user_balance = profile['balance'].strip('$').replace(',', '')
    print(user_balance)
    balance_ls.append(user_balance) #Append puts these items into a list (balance_ls)
    
print (min(balance_ls))

#for profile in profiles:
    if profile['balance'].strip('$').replace(',','') == min(balance_ls):
        print(f'User {profile["name"]} has the least amount of cash: {profile["balance"]}')

# User with the highest balance

for profile in profiles:
    if profile['balance'].strip('$').replace(',','') == max(balance_ls):
        print(f'User {profile["name"]} has the most amount of cash: {profile["balance"]}')
        
# Most common favorite fruit

fruits = []

for profile in profiles:
    print(profile['favoriteFruit'])
    fruits.append(profile['favoriteFruit'])
    
# Least most common favorite fruit

min(fruits, key=fruits.count)

# Total number of unread messages for all users

sum_messages = 0

for profile in profiles:
    message = profile['greeting'].split(' ')
    for word in message:
        if word.isdigit():
            sum_messages = sum_messages + int(word)
            
sum_messages