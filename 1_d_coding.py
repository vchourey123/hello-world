string = "sample.txt"
let = "t"
count = 0
for i in range(len(string)):
	if let == string[i]:
		count = count + 1
	else:
		pass
print(count)
