
number = 56 #Integer
second = 43.12 #FLoat
greeting = "Hello there" #String
isPythongInteresting = True #Boolean

#Data Structures - Multiple values stored in a single variable
cars = ["toyota", "nissan", "porsche"] #List - Ordered and changeable
fruits = ("banana", "orange", "apple") #Tuple - Ordered but unchangeable
countries = {"Kenya", "Tunisia", "Algeria"} #Set - Unordered & unchangeable
student = {
    # key   :   Value
    "firstname": "Reuben",
    "age": 205,
    "course": "Web Development",
    "nationality": "Kenyan",
}                           #Dictionary - Key, value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["course"])

print(number)
print(second)
print(isPythongInteresting)

#Determining a datatype
print(type(student))
print(type(countries))

#Typecasting - Converting 1 data type into another
print(float(number)) #convert int(number) to float
print(int(second)) #convert float(second) to int