chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

money = int(input())
animal = ''
amount = 0

if money >= sheep:
    animal = 'sheep'
    amount = money // sheep
elif money >= cow:
    amount = money // cow
    if amount == 1:
        animal = 'cow'
    else:
        animal = 'cow'
elif money >= pig:
    amount = money // pig
    if amount == 1:
        animal = 'pig'
    else:
        animal = 'pigs'
elif money >= goat:
    amount = money // goat
    if amount == 1:
        animal = 'goat'
    else:
        animal = 'goats'
elif money >= chicken:
    animal = 'chicken'
    amount = money // chicken
    if amount == 1:
        animal = 'chicken'
    else:
        animal = 'chickens'

if amount == 0:
    print(None)
else:
    print(str(amount) + " " + animal)
