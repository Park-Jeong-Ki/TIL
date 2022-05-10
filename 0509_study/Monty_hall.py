import random

door = ['a','b','c']
no_change = 0
change = 0

trial = 100000

for _ in range(trial):
    car = random.randint(0,2)
    player_choice = random.randint(0,2)

    empty_door = []

    for i in range(3):
        if i!=player_choice and i != car:
            empty_door.append(door[i])

    com = random.sample(empty_door, k=1)[0]

    if player_choice == car:
        no_change += 1

    empty_door.remove(com)


    if not empty_door:
        change += 1
            
print('case1:', no_change/trial, '%')
print('case2:',change/trial, '%')   
