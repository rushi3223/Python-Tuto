'''''def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
'''''''''
current_price = int(input("Enter the current price of the stock: "))
yday_price = int(input("Enter the price of the stock yesterday: "))

diff = int(current_price) - int(yday_price)

print(diff)

price1 = 1000
price2 = 5000

total = price1 + price2
print(total)             #explicit

price2 = 200
price1 = "100"
total = int(price1) + price2
print(total)             #explicit

#literals

#binary literal
binary_literal = 0b1010
print(binary_literal)  # 10
#octal literal
octal_literal = 0o12
print(octal_literal)   # 10
#decimal literal
decimal_literal = 10
print(decimal_literal)  # 10
#hexadecimal literal    
hexadecimal_literal = 0xA
print(hexadecimal_literal)  # 10
#float literal
float_literal = 10.5
print(float_literal)  # 10.5
#complex literal
complex_literal = 3 + 4j
print(complex_literal)  # (3+4j)
#string literal
string_literal = "Hello, World!"

#using this for string
#' '
#"  "
#''' '''

print(string_literal)  # Hello, World!
#boolean literal
boolean_literal = True
print(boolean_literal)  # True
# None literal
none_literal = None
print(none_literal)  # None

#unicode str
unicode_str = "Hello, \u2602 World!"  # Unicode character for umbrella
unicode_str1= "rushi \u0001\u0002\u0003"
print(unicode_str1)  # rushi 
print(unicode_str)  # Hello, ☂ World!
