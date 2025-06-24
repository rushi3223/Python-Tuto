entry = 100
exite = 150

# Logical Operators     > = grater than, < = less than, == equal to, != not equal to


# and
print(entry >50 and exite > 100)   #   true only if both sides are true
print(entry == 100 and exite < 100)  # False

# or
print(entry > 100 or exite > 100)  # True        true if is one side is true
print(entry < 100 or exite > 100)  # True

# not
print(not(entry > 100))  # true           its reverses the truth value
print(not(entry < 100))  # True
print(not(entry == 100))  # False
print(not(exite != 150))  # True
