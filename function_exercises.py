### 1. Define a function named is_two. It should accept one input and return 
### True if the passed input is either the number or the string 2, False otherwise.

def is_two(n):
    if n == (2 or 'two' or 'Two' or '2'):
        return True
    else:
        return False
    
## 2. Define a function named is_vowel. It should return True if 
## the passed string is a vowel, False otherwise.

def is_vowel(word):
    if word in ('aeoiuAEIOU'):
        return True
    else:
        return False
    
## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    if is_vowel(x) == True:
        return False
    else:
        return True


## 4. Define a function that accepts a string that is a word. The function should capitalize the first letter 
# of the word if the word starts with a consonant.

def capital_help(string):
    if string [0] not in 'aeiou':
        string = string[0].upper() + string[1:]
    return string

## 5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage,bill_total):
    tip_amount = tip_percentage * bill_total
    total_cost = tip_amount + bill_total
    if tip_percentage > 1:
        print('Enter tip percentage in decimal')
    if tip_percentage > 0 and  tip_percentage < 1:
        return total_cost

## 6.  Define a function named apply_discount. It should accept a original price, and a discount percentage, and 
# return the price after the discount is applied.

def apply_discount(or_price, disc_percentage):
    total_discount = or_price * disc_percentage
    total_price = or_price - total_discount
    return total_price


## 7. Define a function named handle_commas. It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.

def handle_commas(string):
    string = string.replace(',', '')
    return int(string)
    

## 7. Define a function named get_letter_grade. It should accept a number and return the letter 
# grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade > 87:
        return 'A'
    if grade < 88 and grade >79:
        return 'B'
    if grade <79 and grade >66:
        return 'C'
    if grade <67 and grade >59:
        return 'D'
    else:
        return 'F'
    
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0


## 8. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    for i in "aeiouAEIOU":
            string = string.replace(i,"")
    return string


##9. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    ##anything that is not a valid python identifier should be removed

def normalize_name(string):
    string = string.lower()
    string = string.strip()
    string = string.replace(' ', '_')
    return string



##10 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the
# cumulative sum of the numbers in the list.
## cumulative_sum([1, 1, 1]) returns [1, 2, 3]
## cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

