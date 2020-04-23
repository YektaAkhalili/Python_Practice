original_list = ["first", "second", "third"]
print("original list: ", original_list)
original_list[0] = "CAPITALFirst"
print("modified list: ", original_list)
original_list.append("fourth_added")
print("added something to the list: ", original_list)

for i in range(3):
	list_new = ["five", "six", "seven"]
	original_list.append(list_new[i])

print("three things added now: ", original_list)	

# randomly add something in a position 
original_list.insert(0, "Random")
print("Adding something to the front: ", original_list)

# removing stuff according to position 
del(original_list[0]) #this should get rid of "Random"
print("Removing the first element: ", original_list)

# what if I don't want to totally get rid of something? 
favorite_Characters = ["Dolores", "Ford", "William"]
print("Some of my favorite characters from Westworld: ", favorite_Characters)
pop_william = favorite_Characters.pop()
print("One of them was a bad person: ", pop_william)
print("So these are my absolute most favorites: ", favorite_Characters)

# you can use pop(position) too 
favorite_Characters.remove("Ford")
print("The ultimate favorite is: ", favorite_Characters)
