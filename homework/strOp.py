string1 = "My first string"
string2 = "My second string"

#print(string1 + 1)
# //Type Error: can only concatenate str to str
#print(string1 + " and " + string2)
# //My first string and My second string

#print(string1 - 1)
# //TypeError: unsupported operand type(s) for -: 'str' and 'int'
#print(string1 - string2)
# //TypeError: unsupported operand type(s) for -: 'str' and 'str'

#print(string1 * 5)
# //My first stringMy first stringMy first stringMy first stringMy first string
#print(string1 * string2)
# //TypeError: can't multiply sequence by non-int of type 'str'

#print(string1 / 5)
# //TypeError: unsupported operand type(s) for /: 'str' and 'int'
#print(string1 / string2)
# //TypeError: unsupported operand type(s) for /: 'str' and 'str'