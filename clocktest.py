import RPi.GPIO as GPIO # import RPi.GPIO module
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN)
GPIO.setup(38, GPIO.OUT)

def loadData():
	##loads data from encrypted text 

def saveData():
	##saves data and encrpyts on reboot

def checkForWater(): ## checks water sensor
	if (GPIO.input(40)): 
		if firstOpen == 0 :
            		firstOpen = time.perf_counter()
		return true
	else:
		return false

def valveOpen(): ## sends positive output to open valve
	GPIO.output(38, 1)

def valveClose(): ## sends negative output to close valve
	GPIO.output(38, 0)
	
def timer(timeVar): ## function that can be used to count time in seconds and store in a given variable
	if timeVar == 0:
		holdTime = time.perf_counter()
		sleep(0.1)
		holdTime = time.perf_counter()
		timeVar = holdTime
	else:
		timeVar = time.perf_counter() - timeVar
		
	return timeVar

try:
	##loadData()
	startTime = time.perf_counter()
	dayTimer = 0
	valveOpenTime = 0
	MAX_OPEN_SECONDS = 30
	while True
        	dayTimer = timer(dayTimer)
        	while checkForWater() == true && valveOpenTime < MAX_OPEN_SECONDS :
          		valveOpenTime = timer(valveOpenTime);
                	valveOpen()
		valveClose()
        	sleep(0.1)
		
finally: 
	GPIO.cleanup()
	##saveData()
	##Reboot
