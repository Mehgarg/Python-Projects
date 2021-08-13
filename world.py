file = open("world.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)
 
# --- Linear search
key = "Portuguese"
 
i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1
 
if i < len(name_list):
    print( "The name is at position", i)
else:
    print( "The name was not in the list." )
    
file.close()

# Program to sort alphabetically the words form a string provided by the user

# change this value for a different result
my_str = "Spanish English Hindi Arabic Portuguese Russian Mandarin German Vietnamese Cantonese"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)

    
