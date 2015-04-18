import datetime
import RPi.GPIO

ypins = [17, 18, 27, 22, 23, 24, 25]
xpins = [5, 6, 12]

def setArray(myInt, array):
	asBinary = "{0:b}".format(myInt).zfill(7)
	for i in range(0, 7):
		if (asBinary[i] == "0"):
			array[i] = False
		else:
			array[i] = True


for i in xpins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

for i ypins:
    GPIO.setup(i, GPIO.IN)
    GPIO.output(i, False)
	
grid = [[0 for x in range(7)] for x in range(3)] 

now = datetime.datetime.now()
setArray(now.hour, grid[0])
setArray(now.minute, grid[1])
setArray(now.second, grid[2])

for i in range(0, 7):
    for j in range(0, 3):
        

print(len(grid))
print(grid)
