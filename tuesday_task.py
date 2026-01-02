# 1.Find the smallest word in a sentence.
# Input: "Python is super powerful"
# Output: is
# words = "Python is super powerful"
# word_list = words.split( )
# smallest_word = min(word_list, key=len)
# print(smallest_word)

# words = "python is super powerful"
# words_list = words.split()
# highest_word = max(words_list, key=len)
# print(highest_word)


# 2. A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True
# [2,2,5] → False (because 2 is NOT less than 2)
# [10,5,6] → False (because 5 < 10)
# num_list = [9,10,11,12,18,90,28,30]
# is_increasing = True
# for i in range(1,len(num_list)):
#     if num_list[i] <= num_list[i-1]:
#         is_increasing = False
#         break
# print(is_increasing)


# 3. Reverse characters only at even index positions Indices: 0,2,4,6,...
# Input: "abcdefg" Even positioned letters: a, c, e, g → reverse → g, e, c, a
# Final Output: "gbecdfa"
# word = "abcdefghij"
# even_chars = []
# for i in range(len(word)):
#     if i % 2 == 0:
#         even_chars.append(word[i])
# even_chars.reverse()
# result = ""
# even_index = 0
# for i in range(len(word)):
#     if i % 2 == 0:
#         result += even_chars[even_index]
#         even_idex += 1
#     else:
#         result += word[i]
# print(result)


# 4. Replace characters at odd indexes with *.
# Example: "Hello" → "h*l*o" (edited) 
# world = "hello"
# result = ""
# for i in range(len(world)):
#     if i % 2 != 0:
#         result += "*"
#     else:
#         result += world[i]
# print(result)


