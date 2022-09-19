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
