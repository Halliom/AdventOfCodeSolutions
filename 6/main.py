grid = {}
gridPart2 = {}

def parseInstruction(s):
    instruction = {}
    leftArg = s[:s.index("through") - 1]
    rightCoord = s[s.index("through") + 8:]
    leftTokens = leftArg.split(" ")
    action = ""
    leftCoord = ""
    if len(leftTokens) > 2:
        action = leftTokens[0] + leftTokens[1]
        leftCoord = leftTokens[2]
    else:
        action = leftTokens[0]
        leftCoord = leftTokens[1]

    instruction["action"] = action
    instruction["beginCoord"] = (int(leftCoord.split(",")[0]), int(leftCoord.split(",")[1]))
    instruction["endCoord"] = (int(rightCoord.split(",")[0]), int(rightCoord.split(",")[1]))
    return instruction

def doInstruction(s, firstpart=True):
    instruction = parseInstruction(s)
    for i in range(instruction["beginCoord"][0], instruction["endCoord"][0] + 1):
        for j in range(instruction["beginCoord"][1], instruction["endCoord"][1] + 1):
            if not (i, j) in grid:
                if firstpart:
                    grid[(i, j)] = False
                else:
                    grid[(i, j)] = 0
            if instruction["action"] == "toggle":
                if firstpart:
                    grid[(i, j)] = not grid[(i, j)]
                else:
                    grid[(i, j)] += 2
            if instruction["action"] == "turnon":
                if firstpart:
                    grid[(i, j)] = True
                else:
                    grid[(i, j)] += 1
            if instruction["action"] == "turnoff":
                if firstpart:
                    grid[(i, j)] = False
                else:
                    grid[(i, j)] = grid[(i, j)] - 1 if grid[(i, j)] >= 1 else 0

with open("input.txt") as f:
    # PART 1
    for line in f:
        doInstruction(line)
    print(sum(1 if grid[key] else 0 for key in grid))

    # PART 2
    f.seek(0) # reset the file pointer to the start of the file
    grid = {}
    for line in f:
        doInstruction(line, False)
    print(sum(grid[key] for key in grid))
