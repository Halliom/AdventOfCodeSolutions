goodVowels = 'aeiou'
badCombos = ['ab', 'cd', 'pq', 'xy']

# PART 1
def isGoodPart1(s):
    goodVowelsCount = 0
    for c in s:
        if c in goodVowels:
            goodVowelsCount += 1

    if not goodVowelsCount >= 3:
        return 0

    badCombo = False
    hasPair = False
    for i in range(len(s) - 1):
        pair = s[i:i + 2]
        if pair in badCombos:
            badCombo = True
        if pair[0] == pair[1]:
            hasPair = True
    if not badCombo and hasPair:
        return 1
    else:
        return 0

# PART 2
def isGoodPart2(s):
    pairs = []
    double = False
    for i in range(len(s) - 1):
        if s[i:(i + 2)] in s[i + 2:]:
            double = True
            break
    if not double:
        return 0

    interleaved = False
    previousChars = ['-', '-']
    for c in s:
        if c == previousChars[1]:
            interleaved = True
            break
        previousChars[1] = previousChars[0]
        previousChars[0] = c

    if interleaved:
        return 1
    else:
        return 0

goodStrings1 = 0
goodStrings2 = 0
with open("input.txt") as f:
    for line in f:
        goodStrings1 += isGoodPart1(line)
        goodStrings2 += isGoodPart2(line)
    print("Good strings, part 1: " + str(goodStrings1))
    print("Good strings, part 1: " + str(goodStrings2))
