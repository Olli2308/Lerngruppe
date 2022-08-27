age = 35

if age >= 30 and age <= 39:
    print("Diese Person ist in ihren 30-ern")

age = 45
if age < 30 or age >= 40:
    print("Diese Person ist nicht in ihren 30-ern")

age = 25
print(age < 30)

above_30 = age >= 30
print(above_30)

age = 25
above_20 = age >= 20
print(above_20)
if age >= 20:
    print("if-Abfrage wurde ausgeführt")

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

country = "US"
age = 25

if (country == "US" and age >= 21) or (country != "US" and age >= 18):
    print("Diese Person darf Alkohol trinken")
