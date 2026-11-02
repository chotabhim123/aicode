
location = 'A'
rooms = {'A': 'Dirty', 'B': 'Dirty'}

while 'Dirty' in rooms.values():

    print("Location:", location)

    if rooms[location] == 'Dirty':
        print("Action: Suck")
        rooms[location] = 'Clean'

    elif location == 'A':
        print("Action: Move Right")
        location = 'B'

    else:
        print("Action: Move Left")
        location = 'A'

print("Both rooms are Clean!")
