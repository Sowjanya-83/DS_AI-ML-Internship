friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
intersection = friend_a&friend_b
print("Common interests:",intersection)
union=friend_a|friend_b
print("All interests:",union)
difference=friend_a-friend_b
print("Interests unique to Friend A:",difference)