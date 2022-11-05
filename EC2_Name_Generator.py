
#Need to get 2 inputs and utilize them inside a loop 
#use the 2 inputs the user givez to create a random name for the ec2 instance 


import random


counter = 0


EC2_amount = input("List the number of EC2 Instances needed: ")
EC2_department = input("What Department is this for: ")

naming_list = []

for counter in EC2_amount:
    unique_name =   #Research how to generate random characters with random library
    counter += 1
    naming_list.append((unique_name, EC2_department))

