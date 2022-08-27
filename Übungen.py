"""continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

for i in continents:
    print(" ",i)#


def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))"""


def number_group(number):
  if number >0:
    return "Positive"
  elif number <0:
    return "Negative"
  else:
    return "Zero"

number_group(5)
print(number_group(5))
#print(number_group(10)) #Should be Positive
#print(number_group(0)) #Should be Zero
#print(number_group(-5)) #Should be Negative
