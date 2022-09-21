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
    if type(word) == str:
        if len(word) == 1:
            return word.lower() in list('aeiou')
        else:
            return False
    else:
        return False
    
## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    if is_vowel(x) == True:
        return False
    else:
        return True
    
#Shorter way

def is_consonant(x):
    if is_vowel(x) == True:
        return False
    else:
        return True


## 4. Define a function that accepts a string that is a word. The function should capitalize the first letter 
# of the word if the word starts with a consonant.

def capital_help(string):
    if type(string) == str:
        if is_consonant(string[0]):
            return string.capitalize()
        else:
            return string
    else:
        return string

## 5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(bill,tip_percent = 0.2):
    return bill * tip_percent

## 6.  Define a function named apply_discount. It should accept a original price, and a discount percentage, and 
# return the price after the discount is applied.

def apply_discount(or_price, discount = 0.0):
    return or_price - or_price * discount


## 7. Define a function named handle_commas. It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.

def handle_commas(string):
    if type(string) == str:
        return int(string.replace(',', ''))
    else:
        return string
    

## 7. Define a function named get_letter_grade. It should accept a number and return the letter 
# grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade > 87:
        return 'A'
    elif grade >79: #use elif instead of if because you want it to stop when returns true
        return 'B'
    elif grade >66:
        return 'C'
    elif grade >59:
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

## OR

def remove_vowels(string):
    new_word = '' #local variable for this function
    for letter in string: # for loop because you want to keep going through the string
        if not is_vowel(letter):
            new_word += letter
    return new_word


##9. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    ##anything that is not a valid python identifier should be removed

def normalize_name(string): # use isidentifier() function
    newstring = ''
    for letter in string:
        if letter.isidentifier() or letter == ' ':
            newstring += letter
    return newstring.strip().lower().replace(' ', '_') #return newstring after you've completed functions


##10 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the
# cumulative sum of the numbers in the list.
## cumulative_sum([1, 1, 1]) returns [1, 2, 3]
## cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


def cumilative_sum (lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]


