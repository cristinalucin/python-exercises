### 1. Define a function named is_two. It should accept one input and return 
### True if the passed input is either the number or the string 2, False otherwise.

def is_two(n):
    if n == (2 or 'two' or 'Two' or '2'):
        return True
    else:
        return False
    
## 2. Define a function named is_vowel. It should return True if 
## the passed string is a vowel, False otherwise.

def is_vowel(entry):
    if entry in ('aeoiuAEIOU'):
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

def cap_help(x):
    first_char = x[0] # reads entry as a string, position 0
    if is_consonant(first_char): #calls is_consonant
        return x.capitalize()
    else:
        return x


## 5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(bill_total, tip_percentage):
    if tip_percentage > 0 and tip_percentage < 1:
        return bill_total * (1 + tip_percentage)
    elif tip_percentage > 0 and tip_percentage < 100:
        return bill_total * (1 + tip_percentage/100)
    return bill_total


Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
## 6. Define a function named handle_commas. It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.

def handle_commas(str_with_commas):
    string = ''
    for s in str_with_commas:
        if s != ',':
            string = string + s
            #print(string)
    return int(string)

## 7. Define a function named get_letter_grade. It should accept a number and return the letter 
# grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade < 60:
        return 'f'
    elif grade >= 60 and grade < 67:
        return 'd'
    elif grade >= 67 and grade < 80:
        return 'c'
    elif grade >= 80 and grade <= 87:
        return 'B'
    else:
        return 'A'


## 8. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    newstr = word
    for x in vowels:
        newstr = word.replace(x,"")
        return newstr


##9. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    ##anything that is not a valid python identifier should be removed



##10 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the
# cumulative sum of the numbers in the list.
## cumulative_sum([1, 1, 1]) returns [1, 2, 3]
## cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]