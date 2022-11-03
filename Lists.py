var_list = []

print(type(var_list))

var_list.append(493)
var_list.append('809')
var_list.append(151)

print(var_list)

print(var_list[2])
print(var_list[-1])

print(len(var_list))

#Provides a list of built-in fucntions that can be used with that particular data type
print(dir(var_list))


#Range fucntion gives us back a list of numbers
numbers = [0,1,2,3,4,5,6,7,8,9,10]

print(numbers)
numbers = list(set(numbers))

print(list(range(0,15)))

for number in numbers:
    print(number)
    
for i in range(0,20):
    print(i)