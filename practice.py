string1 = "Hello World!"
string2 = "foo"
stringA = "aaa"
stringB = "bbbbb"


def function1(string):
    return string[::-1]


def function2(string):
    newString = ""
    for letter in string:
        newString = letter + newString
    return newString


def function3(string):
    newString = ""
    l = len(string)
    for x in range(l):
        newString += string[l-(x+1)]
    return newString


def function4(string1, string2):
    newString = ""
    if len(string1) <= len(string2):
        s = string1
        l = string2
    else:
        s = string2
        l = string1 
    for i in range(len(s)):
        newString += s[i]
        newString += l[i]
    for j in range(len(l) - len(s)):
        newString += l[len(s) + j]
    return newString

print(function1(string1))
print(function2(string1))
print(function3(string1))
print(function4(string1, string2))
print(function1(function4(stringA, stringB)))




