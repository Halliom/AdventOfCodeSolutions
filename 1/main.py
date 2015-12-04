# PART 1
instr = ""
with open("test.txt", "r") as f:
	instr = str(f.read())

# Cheeky one-liner
print(sum(1 if (c == '(') else -1 for c in instr))

# 2nd part
floor = 0
for i in range(len(instr)):
	if instr[i] == "(":
		floor += 1
	else:
		floor -= 1
	if floor < 0:
		print(i + 1)
		break

# Can also be done in a one-liner but it's quite long
# floorNumber = min(i if (eval(instr[:i].replace("(", "+1").replace(")", "-1")) == -1) else 9999 for i in range(1, len(instr)))
