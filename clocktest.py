import RPi.GPIO as GPIO # import RPi.GPIO module
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN)
GPIO.setup(38, GPIO.OUT)

def loadData():
	##loads data from encrypted text file

def checkForWater(): ## checks water sensor
	if (GPIO.input(40)): 
		return true
	else:
		return false

def valveOpen(): ## sends positive output to open valve
	GPIO.output(38, 1)

def valveClose(): ## sends negative output to close valve
	GPIO.output(38, 0)

	startTime = time.perf_counter()
	firstOpen = 0;
	valveTime = 0;

try:
    while(true){

        dayCounter = perf_counter() - dayCounter
        waterSensor = checkForWater();
        while(waterSensor == true && valveTime < 30min){
            valveTime = perf_counter - valveTime;
            if(valveOpen == false){
                valveOpen()
            }
        }
        if(valveOpen == true){
            valveClose()
        }
        sleep(x)
    }

    checkForWater{
        if(water && firstOpen == 0){
            firstOpen = perf_counter
            return true;
        }
        else if(water){
            return true;
        }
        else{
            return false;
        }
    }
finally: GPIO.cleanup()
