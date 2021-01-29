import json 

#json to Python ----------------------------------
print("Here we convert Json to Python") 
x = '{"name":"John", "age":30, "city":"New York"}'

#Parse it here
y = json.loads(x)

#Print out python dictionary 
print(y["age"])



#Python to json ---------------------------------
print("Here we convert Python to json") 
x = {
    "name": "John",
    "age": 30, 
    "city": "New York" 
}

#convert into JSON: 
y = json.dumps(x)

#JSON string result
print(y)


#Conversions from Python to JSON 

#dict   Object 
#list   Array 
#tuple  Array 
#str    String 
#int    Number 
#float  Number 
#True   true 
#False  false 
#None   null 

#Convert a python object containing all the legal data types: 

print("Here we convert a python object containing all the legal data types") 
x = {
    "name": "John", 
    "age": 30, 
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"), 
    "pets": None, 
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

