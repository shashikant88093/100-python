print("Welcome to Treasure Island.")
print("your mission is to find the treasure.")

direction = input('You are at a cross road. Where do you want to go ? Type "left" or "right" ')

if direction == "left":
    waytoreachIsland = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. type "swim" to swim across \n')
    if waytoreachIsland == "wait":
        print("you arrive at the island unharmed.\n")
    else:
        print("You will killed by corcodile")
else:
    print("You can't be reach the island")