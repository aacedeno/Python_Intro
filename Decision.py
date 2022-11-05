import random

number = random.randint(0,10)
thresh = 3      # be careful of hard code 

print(number)

if (number > thresh):
    print("big number")
elif (number < thresh):
    print("small number")
elif (number > thresh):
    print("really big number")
else:   #elif (number ==6)
    print("number is, ", str(thresh))
    
if (number > 8):
    print("really big number")