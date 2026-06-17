#String"s
str1 = "alpha"
str2 = 'beta'
str3 = '''gamma string'''
str4 = """delta string"""

# Numbers
num1 = 123
float1 = 3.14
complex1 = 2 + 3j

# List / Collection of multi data types, enclosed in square brackets,Mutable

first_list = [str1, "Devops", 47, num1 ,1.5]

#printing a List

print(first_list)

# Tuple / Collection of multi data types, enclosed in round brackets,Immutable
first_tuple = (str1, "Devops", 47, num1, 1.5)
print(first_tuple)


# Dictionary / Collection of key value pairs, enclosed in curly brackets,Mutable

first_dictionary = {"name": "Abhishek", "age": 23, "skill": "Devops", "Exercises": ["Boxing","Dancing","Jogging"]}

print(first_dictionary)

print("Variable first_list is a:", type(first_list).__name__)
print("Variable first_tuple is a:", type(first_tuple).__name__)
print("Variable first_dictionary is a:", type(first_dictionary).__name__) 

# Boolean / True or False
x = True
y = False
print("Variable x is a:", type(x).__name__)
print("Variable y is a:", type(y).__name__)