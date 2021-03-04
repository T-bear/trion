import RPi.GPIO as GPIO
import time
import os

#Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

#Set up pins for different servos 
servoPIN1 = 17
servoPIN2 = 22 
servoPIN3 = 16 
relayPIN4 = 23

GPIO.setup(servoPIN1, GPIO.OUT)
servoCoffee = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
GPIO.setup(servoPIN2, GPIO.OUT)
servoMilk = GPIO.PWM(servoPIN2, 50) # GPIO 22 for PWM with 50Hz
GPIO.setup(servoPIN3, GPIO.OUT)
servoPlate = GPIO.PWM(servoPIN3, 50) # GPIO 16 for PWM with 50Hz
GPIO.setup(relayPIN4, GPIO.OUT)

svar = False  ######### Choose milk amount ###########
while svar == False:

  milkAmount = int(input("How much milk? (Must be between 0 - 10)" ))
  if(milkAmount < 0 or milkAmount > 10):
    print("Input not permitted")

  else: 
    svar = True 

svar2 = False  ######### Choose coffee amount ###########
while svar2 == False:

  coffeeAmount = int(input("Coffee strength? (Answer must be between 0 - 10)" ) ) 
  if(coffeeAmount < 0 or coffeeAmount > 10):
    print("Input not permitted")

  else: 
    svar2 = True 

svar3 = False   ######### Mug choice ###########
while svar3 == False:
  mugNr = int(input("Choose a mug! (Has to be 1, 2, 3 eller 4)"))   
  if(mugNr < 1 or mugNr > 4):
    print("Input not permitted")

  else:
    svar3 = True

#### Adjustemnt of amounts

print("You chose milkamount: " , milkAmount)
print("You chose coffeamount: " , coffeeAmount)
print("You chose mug-number: " , mugNr)

os.system('cls' if os.name == 'nt' else 'clear')


servoPlate.start(0) # Initialization
servoPlate.ChangeDutyCycle(5)
time.sleep(3.7*(mugNr-1))
    
servoPlate.stop()


GPIO.output(relayPIN4, 1)
time.sleep(5)

GPIO.output(relayPIN4,0)
time.sleep(2)


servoCoffee.start(0) # Initialization
try:
  servoCoffee.ChangeDutyCycle(5)
  time.sleep(coffeeAmount)
  servoCoffee.stop()

except KeyboardInterrupt:
  servoCoffee.stop()

servoMilk.start(0) # Initialization
servoMilk.ChangeDutyCycle(5)
time.sleep(milkAmount)  
servoMilk.stop()


servoPlate.start(0) # Initialization
servoPlate.ChangeDutyCycle(5)
time.sleep(3.7*(4-(mugNr-1)))   
servoPlate.stop()
 

