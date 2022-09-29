#1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not
day_of_the_week = input ('enter_day_of_the_week')

if day_of_the_week.lower() == "monday":
    print('it is monday')
else:
    print('it is not monday')
      
#b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_the_week = input ('enter_day_of_the_week')

if day_of_the_week.lower() in ['saturday', 'sunday']:
    print("It's the weekend")
else:
    print("It's a weekday")
    
#c. create variables and make up values for:
# the number of hours worked in one week:

hours_worked = 40
hourly_rate = 60
total_paycheck = hourly_rate * hours_worked

if hours_worked > 40:
    ot_rate = hourly_rate * 1.5
    ot_hours = hours_worked - 40
    print((40*hourly_rate) + (ot_hours * ot_rate))
else:
    print(total_paycheck)
    

#2. Loop Basics

# a. While 
# Create an integer variable i with a value of 5.
i = 5
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

for n in range(100):
    if n % 2 != 0:
        continue
    print(n)
    if n > 100:
        break
    
## ### Alter your loop to count backwards by 5's from 100 to -10.

for n in reversed(range(-15,105,5)):
    print(n)
    if n < -10:
        break

### Create a while loop that starts at 2, and displays the number squared on each 
### line while the number is less than 1,000,000. Output should equal:
     """""
     2
     4
     16
     256
     65536
    """"
i = 2
while i < 1_000_000:
    print(i)
    i = i ** 2
    
## Write a loop that uses print to create the output shown below:
i = 100

while i >= 5:
    print(i)
    i -= 5
    
## b.  FOR loops


##  i. Write some code that prompts the user for a number, then shows a multiplication table 
##     up through 10 for that number.

number = int(input('Enter a number: '))
# needs to be turned into an integer so its wrapped int()
for i in range (1,11):
    print(f'{number} x {i} = {number*i}')
    
##  ii. Create a for loop that uses print to create the output shown below.
for i in range (1,10):
    print(str(i)*i)
    
## c. Break and Continue

##  i. Write a program that prompts the user for a positive integer. Next write a loop 
# that prints out the numbers from the number the user entered down to 1.
      # the only way you can break a while True is break OR change a variable to false
      
while True: #you have to make sure there is a break, exit condition bc this will keep running
    user_num = input('Please enter a positive number: ')
    
    if user_num.isdigit():
        print('This is a digit')
        if int(user_num) > 0:
            print('The number is positive!')
            break
    
user_num = int(user_num)
for i in range(user_num,0,-1):
    print(i)
    
#### iii. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement 
# to continue prompting the user if they enter invalid input. (Hint: use the isdigit 
# method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

while True: #you have to make sure there is a break, exit condition bc this will keep running
    user_num = input('Please enter a positive number between 1 and 50: ')
    
    if user_num.isdigit():
        print('This is a digit')
        if int(user_num) % 2 != 0:
            print('The number is odd!')
            if (int(user_num) >1 and int(user_num) < 50):
                print('The number is between 1 and 50')
                break
                
user_num = int(user_num)

for i in range(1,50):
    if i == user_num:
        print('Yikes skipping')
        continue # continue is to skip an iteration of a loop
    if i % 2 == 1:
        print(f'Here is an odd number: {i}')
        
#### 3. FIZZBUZZ

#### Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number. For the multiples 
# of five print "Buzz" For numbers which are multiples of both three and five print "FizzBuzz"..

for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
        continue
    if i % 3 == 0:
        print('Fizz')
        continue
    if i % 5 == 0:
        print('Buzz')
        continue
    print(i)
    
### 4. Display a table of powers.

#### Prompt the user to enter an integer. Display a 
# table of squares and cubes from 1 to the value entered. Ask if the user wants to continue.

i = int(input('Enter an integer: '))
for n in range(0, i + 1):
    print(f"{n:3}{n**2:5}{n**3:6}")
    
while True:
    user_num = int(input('Enter an integer: '))

    for i in range(1, user_num+1):
        print(f'{i}   |{i**2}   |{i**3}') ## squares and cubes
    
    user_yn = input('Would you like to continue?')
    if user_yn.lower() != 'y':
        break
        
## 5. Convert given number grades into letter grades

## - Prompt the user for a numerical grade from 0 to 100.
## Display the corresponding letter grade.
##  Prompt the user to continue.
## Assume that the user will enter valid integers for the grades.
## The application should only continue if the user agrees to.

while True:
    user_grade = int(input('What is your numerical grade?'))

    if user_grade >= 88:
        print('A')
    elif user_grade >= 80:
        print('B')
    elif user_grade >= 67:
        print('C')
    elif user_grade >= 60:
        print('D')
    else:
        print('F')
        
    user_yn = input('Would you like to continue? ')
    if user_yn.lower() != 'y':
        break
        
## 6 Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary 
# in the list should have the keys title, author, and genre. Loop through the list and print out information about 
# each book.
## Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books 
## in that genre.

user_genre = input('Enter a genre: ')
for book in books:
    if book['genre'] == user_genre:
        book['title']

