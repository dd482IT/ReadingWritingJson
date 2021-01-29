#this small program takes json data from a file and changes each usernames password to hahahahha
#original code is from Kalle Hallden from his video "Python Projects For Beginners"

#first the file is opened using open and each data point is kept as f 
#users are loaded in as f and an attribute is pulled
#the password attribute is changed
#the new value for password is then jumped into users stored as f



import json

json_file = input("insert the file name: ")
users = {} 
with open(json_file) as f: 
    users = json.load(f)
print(users['username'])
print(users['password'])

users['password'] = 'hahahaha'
with open('users.json', 'w') as f: 
        json.dump(users, f) 
print("New password is: " + users['password'])

