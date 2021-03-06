#https://realpython.com/python-json/

import json 
import requests

respone = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response)

#Map of userId to number of complete TODOS for that user 
todos_by_user = {} 

#Increment complete TODOS count for each user
for todo in todos:
    if todo["completed"]:
        try: 
            #Increment the exisiting user's count
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            #This user has not been seen. Set their count to 1. 
            todos_by_user[todo["userId"]] = 1


# Create a sorted list of (userID, num_complete) pairs 
top_users = sorted(todos_by_users.items(),
                key=lambda x: x[1], reverse=True)

#Get the maximum of complete TODOs
max_complete = top_users[0][1]

#Create a list of all users who have completed 
#the maximum number of TODOs 

users = []
for user, num_complete in top_users: 
    if num_complete < max_complete: 
        break
    users.append(str(user)) 

max_users = " and ".join(users) 

#Define a function to filter out completed TODOS
#of users with max completed TODOS

def keep(todo):
    is_completed = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count 

#Write filitered TODOs to file 

with open("filtered_data_file.json", "w") as data_file: 
    filitered_todos = list(filter(keep, todos)) 
    json.dump(filtered_todos, data_file, indent=2)


