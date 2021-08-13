file = open('super_villains.txt')
 
for line in file:
    line = line.strip()
    print(line)
 
file.close()

# --- Linear search
key = "Morgiana the Shrew"
 
i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1
 
if i < len(name_list):
    print( "The name is at position", i)
else:
    print( "The name was not in the list." )
