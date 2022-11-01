#Empty list that is being populated
aws_services = []

#Three differetn ways to add an item into the aws_services list
aws_services.append("EC2")
aws_services.append("Lambda")
aws_services.append("DynamoDB")
aws_services += ["S3", "SNS", "SQS"]
aws_services.extend(["Fargate", "ECS", "RDS"])

#Prints the list and number of items in list
print(aws_services)
print(len(aws_services))

# Two ways to remove an item from a list
del aws_services[4]
aws_services.remove("ECS")

#Prints the updated version of list and number of items in list
print(aws_services)
print(len(aws_services))


