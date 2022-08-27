#for i in range(0, 10,):
#    if i == 3:
#        continue
#    print(i)
#for i in range(1, 10):
#    if i == 4:
#        break
#    print(i)   

#liste = [4, 6, 7, 2, 4, 6, 7]
#
#s = 0

#for element in liste:
#    s = s + element
#   if s >= 10:
 #       break
#print(s)

####Use for loops when there´s a sequence of elements that you want to iterate

####user wile loops when you want to repeat an action until a condition changes
def to_celsius(x):
    return (x-32)*5/9
#range Start/End/Steps
for x in range(0,101,10):
    print(x, to_celsius(x))