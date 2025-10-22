# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist

sentence = "Emma-is-a-data-scientist"
# # - Solve it using an inbuilt function (split()).
for word in sentence .split('-'):
    print(word)
# - Solve it without using any inbuilt split functions
word = ""  
for char in sentence:
    if char != '-':
        word += char  
    else:
        print(word)  
        word = ""     
    if word:
        print(word)

# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP


# - Using an inbuilt function or slicing
sentence = "python"
for word in sentence:
    print(sentence[::-1])
# # - Without using any inbuilt functions/Slicing
word = "Python"        
reverse_word = ""      

i = len(word) - 1      
while i >= 0:          
    reverse_word += word[i] 
    i -= 1            

# print(reverse_word)

# 3. Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7
sentence = "Hello World"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = 0
for char in sentence:
    if char in consonants:
        count += 1

print("Number of consonants:", count)


# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome

def remove_space(text):
    new_text = ""
    for char in text:
         if char != " ":
             new_text = new_text + char
    print(new_text)
    remove_space("Python is awesome")

# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong

def is_strong_password(password):
    special_characters = "!@#$%^&*"
    count = 0
    for i in password:
        if i in special_characters:
            count += 1
    if len(password) >= 8 and count >= 1:
        print("Password is strong")
    else:
        print("Password is not strong")
        is_strong_password('anto@1234')
        is_strong_password('anto09')
    





   



