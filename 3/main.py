def calcHouses(map):
    # Current house position
    currHouse = (0, 0)
    # A set of all the houses we've visited
    visited = set()
    # Start by delivering a present to the current house
    visited.add(currHouse)
    for c in map:
        if c == '^':
            currHouse = (currHouse[0], currHouse[1] + 1)
        elif c == 'v':
            currHouse = (currHouse[0], currHouse[1] - 1)
        elif c == '>':
            currHouse = (currHouse[0] + 1, currHouse[1])
        elif c == '<':
            currHouse = (currHouse[0] - 1, currHouse[1])
        visited.add(currHouse)
    return visited

with open("input.txt") as f:
    instr = f.read()
# PART 1
    print(len(calcHouses(instr)))
# PART 2
    print(len(calcHouses(instr[0::2]) | calcHouses(instr[1::2])))
    # The reason we subtract is because the robot and santa both deliver to the first house
    # but it is only counted once, therefore we have to subtract 1 so that just santa's present
    # counts.
