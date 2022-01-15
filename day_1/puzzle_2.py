depths = []
with open('../input/day_1.txt') as f:
    lines = f.read().splitlines()
    depths = [int(line) for line in lines]

countIncreasing = 0
depthQueue = []
previousDepthSum = None
for currentDepth in depths:
    # Add the depth to the end of the queue
    depthQueue.append(currentDepth)

    # Check if rolling queue contains 3 elements
    if len(depthQueue) == 3:
        currentDepthSum = 0
        for depth in depthQueue:
            currentDepthSum += depth

        if previousDepthSum is not None:
            if currentDepthSum > previousDepthSum:
                countIncreasing += 1

        previousDepthSum = currentDepthSum

        # Remove the first in the queue
        depthQueue.pop(0)

print(f'Increasing Depths: {countIncreasing}')
