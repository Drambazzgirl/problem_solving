# 1.Given an array nums and an integer K, remove the last K elements from the array and print the remaining elements.Test Case 1:
# Input : nums = [10, 20, 30, 40, 50]
# K = 2
# Output: [10, 20, 30]
# Test Case 2:
# Input: nums = [5, 15, 25]
# K = 5
# Output: Invalid Input
# numbers = [10,20,30,40,50]
# number = 2
# for numbers in (len(number)):
#     if numbers < number:
#         print("invalid input")
    
    





#  2. Given two lists, calculate the total count of odd numbers in each list. Print the list that contains the highest count of odd numbers. If the counts are the same, print "Odd counts are equal".
# Test Case 1:
# Input:
# data_x = [1, 2, 3, 4, 5, 6, 7]
# data_y = [11, 22, 33, 44, 55]
# Output: [1, 2, 3, 4, 5, 6, 7]
# data_x_count = 0
# data_y_count = 0
# for i in data_x:
#     if i % 2 != 0:
#         data_x_count = +1
# for j in data_y:
#         if j % 2 != 0:
#              data_y_count = +1
# if data_x_count > data_y_count:
#     print(data_x)
# elif data_y_count > data_x_count:
#     print(data_y)
# else:
#     print("odd counts equal")



# 3. Given an integer N and an array of N integers, write a program to print all the integers that are divisible by their immediate previous integer in the array.
# Test Case 1:
# Input: [1, 2, 3, 6, 7]
# Output: [2, 6]
# Test Case 2:
# Input: [2, 4, 8, 16]
# Output: [4, 8, 16]
# Test Case 3:
# Input: [5, 7, 11, 13, 17]
# Output: [] (edited)


# Step 1: Initialize counts for both lists
# Step 2: Loop through data_x and count odd numbers
# Step 3: Loop through data_y and count odd numbers
# Step 4: Compare both counts and print result


# nums = [10, 20, 30, 40, 50]
# K = 2

# if K > len(nums):
#     print("Invalid Input")
# else:
#     nums = nums[:-K]
#     print(nums)


### Strings

#### Given a date in String Format , find the month inside the date. If the month number is valid , print `YES` else `NO`

# ```python
# Input: "03/12/1997"
# Output: "Yes"
# here month is 12, so valid

# Input: "31/15/2003"
# Output: "No"
# here month is 15, 

# date = ['09/03/2008','10/20/2330']
# for dates in date:
#     day,month,year = dates.split('/')
#     month = int(month)
#     if  1 <= month <= 12:   
#         print("yes")
#     else:
#         print("No")



### You are given a string s that contains both letters and digits. The following are the requirements:

# 2.- Print all the characters in the order they appear (excluding digits).
# - Then print the sum of all digits present in the string.

# ```python
#test case 1
# Input: abc123
# Output: abc6
# explanation : abc123 - here 123 are the numbers so 1+2+3 = 6
# and remaining letters as it is are abc, so the result is abc6
# test case 2
# Input: AC30BD40
# Output: ACBD7


# count of even numbers
# num_list = [10,9,28,19,40,39,60,90,99]
# count  = 0
# for i in range(len(num_list)):
#     if num_list[i] % 2== 0:
#         count = count +1
#         print(count)



