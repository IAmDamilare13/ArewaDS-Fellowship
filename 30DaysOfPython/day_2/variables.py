print('Day 2: 30 Days of python programming')


#EXERCISE: LEVEL ONE
#Variable Declaration

print("-------------------------------------------------------")
print("Variable Declaration")

first_name = 'Damilare'
last_name = 'Daramola'
full_name = 'Damilare Daramola'
country = 'Nigeria'
city = 'Akure'
age = 27
year = 2024
is_married = False
is_true = True
is_light_on = True

first_name, last_name, country = 'Damilare', 'Daramola','Nigeria'

print(first_name, last_name, country)

print("-------------------------------------------------------")
print("-------------------------------------------------------")

# EXERCISE: LEVEL TWO
# Check data type of variables

print('Question One: Checking data type of variables')
first_name_type = type(first_name)
print('First name data type: ', first_name_type)

last_name_type = type(last_name)
print('Last name data type: ', last_name_type)

full_name_type = type(full_name)
print('Full name data type: ', full_name_type)

country_type = type(country)
print('Country data type: ', country_type)

city_type = type(city)
print('City data type: ', city_type)

age_type = type(age)
print('Age data type: ', age_type)

year_type = type(year)
print('Year data type: ', year_type)

is_married_type = type(is_married)
print('is_married data type: ', is_married_type)

is_true_type = type(is_true)
print('is_true data type: ', is_true_type)

is_light_on_type = type(is_light_on)
print('is_light_on data type: ', is_light_on_type)

print("-------------------------------------------------------")

#QUESTION TWO: Find length of first name and last name
print('Question Two: Find length of first name')

first_name_length = len(first_name)
print('First name length: ', first_name_length)

print("-------------------------------------------------------")

# QUESTION THREE: Compare the lenght of first name and last name
print('Question Three: Compare the length of first name and last name')

first_name_length = len(first_name)
print('First name length is: ', first_name_length)

last_name_length = len(last_name)
print('Last name length is: ', last_name_length)

print("-------------------------------------------------------")

# QUESTION FOUR: Declare of Variables
print('Questions Four to Eleven: Declaration of variables (5 and 4) and carrying out of some mathematical operations')
num_one, num_two = 5, 4

# QUESTION FIVE: Addition Operation
total = num_one + num_two
print('Addition Operation gives', total)

# QUESTION SIX: Subtraction Operation
diff = num_one - num_two
print('Subtracton Operation gives', diff)

# QUESTION SEVEN: Multiplication Operation
product = num_one * num_two
print('Multiplication Operation gives', product)

# QUESTION EIGHT: Division Operation
division = num_one / num_two
print('Division Operation gives', division)

# QUESTION NINE: Modulus Operation
remainder = num_two % num_one
print('Modulus Operation gives', remainder)

# QUESTION TEN: Raise to Power Operation
exp = num_one ** num_two
print('Raise to Power Operation gives', exp)


# QUESTION ELEVEN: Floor Division Operation
floor_division = num_one // num_two
print('Floor Division Operation gives', floor_division)

print("-------------------------------------------------------")

# QUESTION TWELVE: Calculation of area and circumference of a circle

print('Calculate the area and circumference of a circle with radius of 30m')

# Given radius(m) as 30
radius = 30
pi = 3.142 # Constant

#Calculate area
area_of_circle = pi * (radius ** 2)
print('The circle has an area of ', area_of_circle)

#Calculate circumference
circum_of_circle = 2 * pi * radius
print('The circle has a circumference of ', circum_of_circle)

print('Calculate the area of a circle with radius given by user.')

#Taking radius of the circle as input from user
radius_input = input('Input radius of the circle: ')
radius_input = float(radius_input)

#Calculate area with the new radius
new_area_of_circle = pi * (radius_input ** 2)
print('The circle has an area of ', new_area_of_circle)


print("-------------------------------------------------------")

# QUESTION THIRTEEN: Collecting User Input
print('Questions Thirteen: Collect data from user using input function')

#Declaration of varibles

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Which country are you from? ')
age = input('How old are you? ')

print(f'Hello, meet {first_name} {last_name}, he is {age} years of age, and he is from {country}.')

print("-------------------------------------------------------")

# QUESTION FOURTEEN: Checking for Python reserved keywords
print('Questions Fourteen: Checking for Python reserved keywords')
help('keywords')
