# 1. There is an error while reversing the given string. Please identify and correct it.
word = "Python"
rev = ""
for i in range(len(word)):
    rev = word[i] + rev  
print("Reversed:",rev )

# 2. There is an error while counting vowels in the given text. Please identify and correct it.
text = "Education"
count = 0
for ch in text:
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        count = count + 1
print("Vowels:", count)

# 3. There is an error while finding the smallest element in the list. Please identify and correct it.
nums = [9, 5, 3, 8, 1]
min_num = nums[0]
for i in range(1, len(nums)):
    if nums[i] < min_num:
        min_num = nums[i]
print(min_num)

# 4. There is an error while printing alternate elements from the list. Please identify and correct it.
num_list = [10, 20, 30, 40, 50]
for i in range (len(num_list)):
    if i % 2 == 0:
        print(num_list[i])

# 5. There is an error while replacing negative numbers in the list with 0. Please identify and correct it.
nums = [-3, 5, -2, 7]
for i in range (len(nums)):
    if nums[i] < 0:
        nums[i] = 0
print(nums)