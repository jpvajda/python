# notes on how to code in python 

# function with no return statement. 
def say_hi(name, age): 
  print('Hello ' + name + ', you are ' + str(age))

say_hi('Mike', 35) 
say_hi('Steve', 20) 


# function with a return statement 
def cube(num): 
 return num * num * num 

result = cube(4)
print(result)

# If elif & else
is_male = False
is_tall = True

# Or statement 
if is_male or is_tall: 
  print('You are a male, tall or both!')
else:
  print('You are not a male or tall!')

# And Statement 
if is_male and is_tall: 
  print('You are a tale male.')
elif is_male and not(is_tall):
  print('You are a short male.')
elif not(is_male) and is_tall:
  print('You are not a male but tall.')  
else:
  print('You are not a male or not tall!')

# Comparsion if statement 

def  max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:  
      return num3

print(max_num(3,40,5))


## Simple Calculator 

num1 = float(input('Enter first number: '))
op = input('Enter operator: ')
num2 = float(input('Enter 2nd number: '))

if op == "+":
   print(num1 + num2)
elif op == "-":
    print(num1 - num2) 
elif op == "/":
    print(num1 / num2)   
elif op == "*":
    print(num1 * num2) 
else: 
    print('Invalid operator')

    # Dictionary Example 

    monthConversions = { 
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "June": "June",
    "July": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Luck", "Not a valid Key"))


# While Loop Example 

i = 1
while i  <= 10: 
  print(i)
  i = i + 1

print('Done with loop')

# For Loops 

# loop through an array 
friends = ['Jim', 'Karen', 'Kevin']
for friend in friends:
    print(friend)

# loop through a string 
letters = 'Giraffe School'
for letter in letters:
    print(letter)


# loop through a range 
friends = ['Jim', 'Karen', 'Kevin']
for index in range(10):
    print(index)

friends = ['Jim', 'Karen', 'Kevin']
for index in range(3, 10):
    print(index)

# loop with an index 
 friends = ['Jim', 'Karen', 'Kevin']
for index in range(len(friends)):
    print(friends[index])


# access data in a 2D list 

number_grid = [ 
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
   [0]
]

print(number_grid[0][2])


for row in number_grid: 
  for col in row: 
      print(col)

for col in number_grid: 
  for row in col: 
      print(row)

# Try + Except Error handling 

try: 
  answer = 10/0
  number = int(input("Enter a number:"))
  print(number)
except ZeroDivisionError as err: 
  print(err)
except ValueError: 
  print("Invalid: No input provided.")

  # import 
  # used to access functionality from external python files or modules.

  import file_name