#### ---- INPUT ---- ####

# Get INPUT asking for a quote, and ASSIGN to a
# variable called quote
quote = input("What's your favorite inspirational quote?")

# Get INPUT asking who said the quote, and ASSIGN to
# a variable called author
author = input("Who said this? ")


#### ---- BORDERS ---- ####

# Create variable called line1 and ASSIGN it a border:
# "-----~~~~~~~~~***********~~~~~~~~~-----"
line1 = ".--._,-'_`-._,-'_`-._,-'_`-._,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,_,-'_`-,."

# Create variable called line2 and ASSIGN it a border:
# "|| ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~ ||"
line2 =  "/\ \/ ,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._,-' `-._`./ \ \ ."



#### ---- OUTPUT ---- ####

# PRINT a blank line for readability
print("")

# PRINT line1
print(line1)

# PRINT LINE2
print(line2)
# PRINT "    ", CONCATENATED with the quote
print("    " + quote)

# PRINT "        - ", CONCATENATED with the author
print("        - " + author)

# PRINT line2
print(line2)

# PRINT line1
print(line1)
