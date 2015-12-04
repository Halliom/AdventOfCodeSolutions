totalAmountWrappingPaper = 0
totalAmountRibbon = 0
with open("input.txt", "r") as f:
	for line in f:
		# [l, w, h]
		box = [int(line.split("x")[0]), int(line.split("x")[1]), int(line.split("x")[2])]
		# sort() doesn't return the list but sorted() does
		dim = sorted(box)
		# Remove the item at the end of the list (since the list is sorted
		# this will be the largest number, leaving us with the two smallest)
		dim.pop()
		# 2*l*w + 2*w*h + 2*h*l
		totalAmountWrappingPaper += 2*box[0]*box[1] + 2*box[1]*box[2] + 2*box[2]*box[0] + (dim[0] * dim[1])
		totalAmountRibbon += sum(dim) * 2 + box[0] * box[1] * box[2]

# PART 1
print(totalAmountWrappingPaper)
# PART 2
print(totalAmountRibbon)
