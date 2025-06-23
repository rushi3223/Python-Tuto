entry = 100
exite = 150

# Relational Operators           > = grater than, < = less than, == equal to, != not equal to

# greater than
print(entry > exite)  # False

# less than
print(entry < exite)  # True
# greater than or equal to
print(entry >= exite)  # False
# less than or equal to
print(entry <= exite)  # True
# equal to
print(entry == exite)  # False
# not equal to
print(entry != exite)  # True   
# identity operators
print(entry is exite)  # False
print(entry is not exite)  # True
# membership operators
my_list = [100, 200, 300]
print(entry in my_list)  # False
print(exite in my_list)  # False
print(entry not in my_list)  # True
print(exite not in my_list)  # True


# bitwise operators
print(entry & exite)  # Bitwise AND
print(entry | exite)  # Bitwise OR
print(entry ^ exite)  # Bitwise XOR
print(~entry)  # Bitwise NOT
print(entry << 2)  # Bitwise left shift
print(entry >> 2)  # Bitwise right shift
# Assignment operators
entry *= 2
entry /= 2
entry += 900
entry -= 100
exite -= 10

entry **= 2  #power of a number
print(entry)  
print(exite) 


# Output the final values
print(f"Final entry value: {entry}")
print(f"Final exit value: {exite}")




