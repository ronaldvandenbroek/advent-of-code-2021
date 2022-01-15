# Import Data
depths = []
with open('../input/day_1.txt') as f:
    lines = f.read().splitlines()
    depths = [int(line) for line in lines]

# Process Data
countIncreasing = 0
previousDepth = depths[0]
for currentDepth in depths:
    if currentDepth > previousDepth:
        countIncreasing += 1
    previousDepth = currentDepth
print(f'Increasing Depths: {countIncreasing}')
