### STRINGS
# - Write a program that takes a string as input and counts the number of uppercase letters in it.
# ```python
# # test case 1
# Input: "HelloWorld"
# Output: 2
# explanation -> H , W are upper case so, output is 2
# sentence = "HelloWoRLD"
# count = 0
# for ch in sentence:
#     if ch.isupper():
#         count = count+1
# print(count)



# - Given a list of numbers, print the list in reverse order without using list slicing ([::-1]).
# ```python
# # test case 1
# Input: nums = [1,3,7,8,9]
# Output: [9,8,7,3,1]
# # test case 2
# Input: nums = []
# Output: []
# ```
# number = [1,3,10,8,9]
# rev = []
# for i in range(len(number)-1,-1,-1):
#     rev.append(number[i])
# print(rev)
        
#            (or)
# number = [1, 3, 7, 8, 9]
# rev = []

# for n in number:
#     rev.insert(0, n)   # Always insert at the front

# print(rev)




# - Write a program that finds the longest word in a given sentence.
#   (Bonus: If you are too studious, try without using `split(" ")` and solve)
# ```python
# # test case 1
# Input: "Johannesburg is the most populous city of South Africa"
# Output: "Johannesburg"
# # based on the word length -> it is Johannesburg
# sentence = "Johannesburg is the most populous city of South Africa"

# words = sentence.split()
# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest word:", longest)

        # (or)
# sentence = "Johannesburg is the most populous city of South Africa"
# longest = ""
# current = ""
# for ch in sentence:
#     if ch == " ":
#         if len(current) > len(longest):
#             longest = current
#         current = ""          
#     else:
#         current += ch         
# if len(current) > len(longest):
#     longest = current
# print(longest)


# - Given a sentence, interchange the words that appear before and after every occurrence of the word `and`.
#  The word `and` should remain in the same position, but the surrounding words must be swapped.
# ```python
# Input: apple and banana
# Output: banana and apple
# s="apple and banana"
# res=s.split(" ")
# final=[]
# for i in range(len(res)-1,-1,-1):
#     if res[i]=="and":
#         final.append(res[i+1])
#         final.append(res[i])
#         final.append(res[i-1])
# print(" ".join(final))







