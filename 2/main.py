totalAmountWrappingPaper = 0 
totalAmountRibbon = 0
with open("input.txt", "r") as f:
	for line in f:
		# l, w, h
		box = [int(line.split("x")[0]), int(line.split("x")[1]), int(line.split("x")[2])]
		dim = sorted(box)
		dim.pop()
		# 2*l*w + 2*w*h + 2*h*l
		totalAmountWrappingPaper += 2*box[0]*box[1] + 2*box[1]*box[2] + 2*box[2]*box[0] + (dim[0] * dim[1])
		totalAmountRibbon += sum(dim) * 2 + box[0] * box[1] * box[2]

print(totalAmountWrappingPaper)
print(totalAmountRibbon)