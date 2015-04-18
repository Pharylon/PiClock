print("Hello import datetime

def setArray(myInt, array):
	asBinary = "{0:b}".format(myInt).zfill(7)
	for i in range(0, 7):
		if (asBinary[i] == "0"):
			array[i] = False
		else:
			array[i] = True

	
grid = [[0 for x in range(7)] for x in range(3)] 

now = datetime.datetime.now()
setArray(now.hour, grid[0])
setArray(now.minute, grid[1])
setArray(now.second, grid[2])

print(len(grid))
print(grid)