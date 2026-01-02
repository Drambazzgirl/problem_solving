# 1.Given a sentence, find and print the shortest word in that sentence.
# sentence = "python makes programming enjoyable"
# shortest_word =" "
# current_word = " "
# for char in sentence:
#     if char != " ":
#         current_word += char
#     else:
#         if shortest_word == " " or len(current_word) < len(shortest_word):
#             shortest_word = current_word
#         current_word = " "
# if shortest_word == " " or len(current_word) < len(shortest_word):
#     shortest_word = current_word
# print(shortest_word)


# 2.print the maximum occurring charecter in a String
# districts = ["Chennai", "madurai", "Villupuram", "Tiruvannamalai", "Bangalore"]
# summer = [100,20,790,800,500]
# winter = [300,900,10.40,90,400]
# monsoon = [200,600,400,700,790]

# season = "winter"

# if season == "summer":
#     season = summer
# elif season == "winter":
#     season = winter
# elif season == "monsoon":
#     season = monsoon
# else:
#     print("invalid season")
#     exit()

# max_value = 0
# max_district = " "

# for i in range(len(districts)):
#     if season[i] > max_value:
#         max_value = season[i]
#         max_district = districts[i]
# print("highest:",max_district)


# districts = ["Chennai", "Madurai", "Coimbatore"]

# summer = [40, 38, 36]
# winter = [25, 70, 20]
# monsoon = [30, 28, 27]

# season = "winter"     # or "winter" or "monsoon"

# # Select the correct list based on season
# if season == "summer":
#     season_list = summer
# elif season == "winter":
#     season_list = winter
# elif season == "monsoon":
#     season_list = monsoon
# else:
#     print("Invalid season")
#     exit()

# max_value = 0
# max_district = ""

# # Find highest temperature district
# for i in range(len(districts)):
#     if season_list[i] > max_value:
#         max_value = season_list[i]
#         max_district = districts[i]

# print("Highest:", max_district)




