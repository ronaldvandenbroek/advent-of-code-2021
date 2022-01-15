# Import Data
commands = []
with open('../input/day_2.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        splitline = line.split(" ")
        splitline[1] = int(splitline[1])
        commands.append(splitline)

# Process Data
positionHorizontal = 0
positionVertical = 0
for command in commands:
    direction = command[0]
    amount = command[1]

    if direction == 'forward':
        positionHorizontal += amount
    elif direction == 'down':
        positionVertical += amount
    elif direction == 'up':
        positionVertical -= amount

print(f'Horizontal Movement: {positionHorizontal}')
print(f'Vertical Movement: {positionVertical}')
print(f'Multiplied Movement: {positionHorizontal * positionVertical}')
