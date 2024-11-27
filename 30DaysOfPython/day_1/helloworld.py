print("EXERCISE: LEVEL TWO")

#Question One: To check python version
print("Question One")
print("To check python version: \n This is done from the comamnd line by typing 'py --version' \n My python version is: Python 3.10.4")

print("-------------------------------------------------------")

#Question Two: Given operands as 3 and 4
print("Question Two")
print("Given operands as 3 and 4. let the first operand be 3 and the second be 4")
#Addition Operation  
a = 3 + 4
print(f"Addition Operation gives: {a}")

#Subtraction Operation
b = 3 - 4
print(f"Subtraction Operation gives: {b}")

#Multiplication Operation  
c = 3 * 4
print(f"Multiplication Operation gives: {c}")

#Modulus Operation  
d = 3 % 4
print(f"Modulus Operation gives: {d}")

#Division Operation
e = 3 / 4
print(f"Division Operation gives: {e}")

#Exponential Operation
f = 3 ** 4
print(f"Exponential Operation gives: {f}")

#Floor Division Operation  
g = 3 // 4
print(f"Floor Division Operation gives: {g}")

print("-------------------------------------------------------")

#Question Three
print("Question Three")

name = "Damilare"
family_name = "Daramola"
country = "Nigeria"
comment = "I am enjoying 30 days of python"

strings = f"Hello, I am {name} {family_name} from {country}, and {comment}"

print(strings)

print("-------------------------------------------------------")

#Question Four: Data Types
print("Question Four")

#Assigned variables
a = 10
b = 9.8
c = 3.14
d = 4 - 4j
e = ['Asabeneh', 'Python', 'Finland']

#Check Data Types
type_a = type(a)
type_b = type(b)
type_c = type(c)
type_d = type(d)
type_e = type(e)
type_name = type(name) # Recalled from previous cell
type_family_name = type(family_name) # Recalled from previous cell
type_country = type(country) # Recalled from previous cell

#Return Data Types
print(f"The data type of {a} is {type_a}")
print(f"The data type of {b} is {type_b}")
print(f"The data type of {c} is {type_c}")
print(f"The data type of {d} is {type_d}")
print(f"The data type of {e} is {type_e}")
print(f"The data type of {name} is {type_name}")
print(f"The data type of {family_name} is {type_family_name}")
print(f"The data type of {country} is {type_country}")

print("-------------------------------------------------------")
print("-------------------------------------------------------")


print("EXERCISE: LEVEL THREE")

#Question One: To check python version
print("Question One")
print("Examples for different Python data types")

#NUMBERS

#Integer
d_int = 22
print(type(d_int))

#Float
d_flt = 2.2
print(type(d_flt))

#Complex
d_cmp = 2 + 2j
print(type(d_cmp))

#String
d_str = "22"
print(type(d_str))

#Boolean
d_boo = True
print(type(d_boo))

#List
d_lst = [2, 2]
print(type(d_lst))

#Tuple
d_tup = (2, 2.2, 22)
print(type(d_tup))

#Set
d_set = {2, 2.2, 22}
print(type(d_set))


#Dictionary
d_dic = {"v1" : "2",
         "v2" : "22",
         "v3" : "2.2"}
print(type(d_dic))

print("-------------------------------------------------------")

print("Question Two")
print("Find the Euclidian distance between (2,3) and (10,8)")

#Assign Variables to each points
p1 = 2
p2 = 10
q1 = 3
q2 = 8

d = (q1 - p1)**2 + (q2 - p2)**2

Distance = print(f"Distance is {d}")