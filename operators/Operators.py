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


# membership operators   in , not in ,# These operators are used to check if a value is present in a sequence (like a list, tuple, or string).
my_list = [100, 200, 300]
print(entry in my_list)  # False
print(exite in my_list)  # False
print(entry not in my_list)  # True
print(exite not in my_list)  # True


# bitwise operators    its a binary operation, it works on bits and performs bit by bit operation
# Bitwise operators work on binary representations of integers.

a = 5
b = 3
# 5 in binary is 101 , # 3 in binary is 011

print(a & b)  # Bitwise AND      base on binary truth table
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)  # Bitwise NOT
print(a << 2)  # Bitwise left shift
print(a >> 2)  # Bitwise right shift


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




