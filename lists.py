# Unpacking


score_list = [80, 95, 30, 78]

print(list(enumerate(score_list))) # returns enumerate object (that contains tuples) at memory location

# Unpacking
# turn object into something you can see by passing it into the tuple or list constructor
score1, score2, score3, score4 = score_list # unpacking - taking a list and other side of =, putting ",,," ... number of values to unpack must be the same
first_score, *rest_of_scores = score_list


for index, score in enumerate(score_list): # enumerate yields count (index) and value
    print(index, score)



# artist_names = ["K","A","R"]

# for name in sorted(artist_names):
#     print(name)



# text = ""
# while text != "stop":
#     text = input("Tell me to stop! ")



# lst = ["a","a","b","a"]

# target_word = "a"
# count = 0
# count_other = 0
# new_list=[]

# for word in lst:
#     if word == target_word:
#         count += 1
#         new_list.append(word) # true filter
#     else:
#         count_other += 1

# print(count) # reduce -- loop through a list and reduce it down to a single value (e.g. count)
# print(new_list) # true filter
