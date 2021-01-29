import json

users = {} 
with open('users.json') as f: 
    users = json.load(f)
print(users['username'])
print(users['password'])

users['password'] = 'hahahaha'
with open('users.json', 'w') as f: 
        json.dump(users, f) 
print("New password is: " + users['password'])

