#Ask User for Name
name = input('What is your name? ')

#Ask User for Age
age = input('How old are you? ')

#Ask User for City
city = input('What city do you live in? ')

#Ask User what they Enjoy
enjoy = input('What activities do you enjoy? ')

#Create Output text
string = "Hi! I am {}, and I am {} years old. I live in {}, and enjoy {}""
output = string.format(name, age, city, enjoy)

#Print Output to screen
print(output)
