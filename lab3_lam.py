# Lam Ngu | Lab 3 | Green

# ticket 1
username = "Lam"
print(len(username)) # 3
# len() counts every character


print(username[0]) # L
last_index = len(username) - 1
print(username[last_index]) # m
# Python indexing starts counting at 0 onstead of 1

print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @{username}!")
# Both will look the same, but f string is way easier because you dont have to close quotation marks alot

#username[0] = "X" #run this, it breaks
#before running it i think it gonna breaks, error and crash
#str' object does not support item assignment
# The right way : print in capital letter using prin(username.upper())
#Immutable means that once a string is created it can not be changed

#ticket 2
feed = ["funny", "happy", "angry"]
print(len(feed)) # 3 "funny" will print first
print(feed[0]) # funny
print(feed[2]) # angry
#i use index 0 to get the first post
feed.append("crazy") # 3
print(feed)
# it sits at 3 because python list starts at 0
feed.pop(0)  # the very first post will get remove, it will end up a to z
feed.sort()
print(feed)
#i used .pop() which remove the item at the index, and .sort() which organize the remainngs in order A to Z

#ticket 3
profile = {"username": "bear", "followers": 923, "verified": True }
print(profile["followers"]) #print 923
# profile[0] # breaks because it tries to search for a key named 0 in the dictionary
# Key Error: 0
# because they look up datat using labels

profile["followers"] = profile["followers"] + 50
profile["bio"] = "hi welcome"
print(profile)
print(profile.get("age")) # this will print nothing
# using .get() is safer because it shows None if it missing instead of giving you error

# ticket 4
everything = f"@{profile["username"]} has {profile["followers"]} followers and {len(feed)} posts. Top post: {feed[0]}"
print(everything)
#it will print @bear has 973 followers and 3 posts. Top post: angry
#i used a dictionary to look up username and followers, i also use a list to get the post count and the caption

