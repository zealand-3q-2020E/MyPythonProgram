from sense_hat import SenseHat
from random import randint
from time import sleep

def getRandomColor():
	return [randint(0,255), randint(0,255), randint(0,255)]

def next(n):
	return (n+1) % 8

def prev(n):
	if n==0:
		return 7
	else:
		return n-1

sense = SenseHat()
x = 4
y = 4
color = getRandomColor()
print("Ready")
sense.clear()
sense.set_pixel(x,y,color)

sleeptime = 0.5

while True:
	orientation = sense.get_orientation()
	pitch = orientation['pitch']
	roll = orientation['roll']
	print("pitch {0} roll {1}".format(pitch, roll))
	moved = False

	if 10 < pitch < 180:
		x = prev(x); moved = True
	elif 180 < pitch < 350:
		x = next(x); moved = True

	if 10 < roll < 180:
		y = next(y); moved = True 
	elif 180 < roll < 350:
		y = prev(y); moved = True

	if moved:
		sense.clear();
		sense.set_pixel(x,y,color)
	sleep(sleeptime) 
	sleeptime = sleeptime*0.9





