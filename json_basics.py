import json 

#json to Python ---------------------------------- 
x = '{"name":"John", "age":30, "city":"New York"}'

#Parse it here
y = json.loads(x)

#Print out python dictionary 
print(y["age"])

#Python to json ---------------------------------

x = {
    
    "name": "John",
    "age": 30, 
    "city": "New York" 
}

#convert into JSON: 
y = json.dumps(x)

#JSON string result
print(y)

