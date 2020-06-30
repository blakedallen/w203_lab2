
import csv
num_r = 0
num_d = 0
num_other = 0
header_row = []
with open("anes_pilot_2018.csv") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for i,row in enumerate(spamreader):
		if i == 0:
			header_row = row
			pid1r = header_row.index("pid1r")
			pid1d = header_row.index("pid1d")
			continue

		v1d = int(row[pid1d])
		v1r = int(row[pid1r])

		answer = "?"
		if v1d > 0:
			if v1d == 1:
				answer = "d"
			elif v1d == 2:
				answer = "r"
		elif v1r > 0:
			if v1r == 1:
				answer = "r"
			elif v1r == 2:
				answer = "d"

		#print(i)
		if answer == "d":
			num_d += 1
		elif answer == "r":
			num_r += 1
		else:
			num_other += 1

print(len(header_row), pid1r, pid1d)
print(num_r, num_d, num_r+num_d+num_other)