import json

x = {
    'name': 'Bill',
    'age': 73,
    'city': 'Seatle'
}

y = json.dumps(x)

print(y)
