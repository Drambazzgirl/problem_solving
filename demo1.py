# 1. Problem: Given an array of integers, count how many numbers are even and how many are odd.
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: { even: 3, odd: 3 }
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd = 0
even = 0
for i  in range (len(num_list)):
    if num_list[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even",even,"Odd",odd)

# 2. Problem: Given an array of integers and a target element, find the indices of its first and last occurrence.
# Example Input: ([5, 2, 3, 5, 7, 5, 8], 5)
# Example Output: { firstIndex: 0, lastIndex: 5 }
def find_first_last_index(arr, target):
    first_index = -1
    last_index = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first_index == -1:
                first_index = i
            last_index = i

    return {"firstIndex": first_index, "lastIndex": last_index}


# 3. Given a string, the task is to reverse the order of the words in the given string.
# Examples:
# Input: s = “hello everyone”
# Output: s = “everyone hello”
# Input: s = “i love programming very much”
# Output: s = “much very programming love i”
def reverse_words(s):
    words = s.split()          
    reversed_words = words[::-1] 
    result = " ".join(reversed_words)  
    return result

















# 3. Given a string, the task is to reverse the order of the words in the given string.
# Examples:
# Input: s = “hello everyone”
# Output: s = “everyone hello”
# Input: s = “i love programming very much”
# Output: s = “much very programming love i”

