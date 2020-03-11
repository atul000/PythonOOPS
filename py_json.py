import json

# sample json
userJSON = '{"first_name": "atul", "last_name": "alex", "Age": 30 }'

# parse to dict
user = json.loads(userJSON)

print(user)

car = {'make': 'Ford', 'model': 'mustang', 'year': 1200}

carJSON = json.dumps(car)
print(carJSON)
