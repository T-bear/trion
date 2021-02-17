import RPi.GPIO as GPIO
import time
import os

#Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

#Set up pins for different servos 
servoPIN1 = 17
servoPIN2 = 22 
servoPIN3 = 16 
servoPIN4 = 23

GPIO.setup(servoPIN1, GPIO.OUT)
servoCoffee = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
GPIO.setup(servoPIN2, GPIO.OUT)
servoMilk = GPIO.PWM(servoPIN2, 50) # GPIO 1337 for PWM with 50Hz
GPIO.setup(servoPIN3, GPIO.OUT)
servoPlate = GPIO.PWM(servoPIN3, 50) # GPIO 1337 for PWM with 50Hz
GPIO.setup(servoPIN4, GPIO.OUT)

svar = False  ######### Choose milk amount ###########
while svar == False:

  milkAmount = int(input("How much milk? (Must be between 0 - 10)" ))
  if(milkAmount < 0 or milkAmount > 10):
    print("Svar ej giltigt.")

  else: 
    svar = True 

svar2 = False  ######### Choose coffr amount ###########
while svar2 == False:

  coffeeAmount = int(input("Coffe strength? (Svar must var mellan 0 - 10)" ) ) 
  if(coffeeAmount < 0 or coffeeAmount > 10):
    print("Svar ej giltigt.")

  else: 
    svar2 = True 

svar3 = False   ######### Mug choice ###########
while svar3 == False:
  mugNr = int(input("Choose mug! (Has to be 1, 2, 3 eller 4)"))   
  if(mugNr < 1 or mugNr > 4):
    print("Svar ej giltigt.")

  else:
    svar3 = True

#### Adjustemnt of amounts

#Standardvalue

stdValueCoffee = 5
stdValueMilk = 5
stdValuePlate = 0


coffeloop = True 

print("Du valde milkamount: " , milkAmount)
print("Du valde coffeamount: " , coffeeAmount)
print("Du valde mugg: " , mugNr)

os.system('cls' if os.name == 'nt' else 'clear')


servoPlate.start(0) # Initialization
#try:
servoPlate.ChangeDutyCycle(5)
    #time.sleep(plateFinal)
time.sleep(3.7*(mugNr-1))
    
#except KeyboardInterrupt:
servoPlate.stop()
  #GPIO.cleanup()


GPIO.output(servoPIN4, 1)

time.sleep(5)

GPIO.output(servoPIN4,0)

time.sleep(2)


servoCoffee.start(0) # Initialization
try:
#  while coffeloop == True:
  servoCoffee.ChangeDutyCycle(5)
   # time.sleep(coffeeFinal)
  time.sleep(coffeeAmount)
  servoCoffee.stop()
#    coffeloop = False

except KeyboardInterrupt:
  servoCoffee.stop()
 # GPIO.cleanup()

servoMilk.start(0) # Initialization
#try:
#  while True:
servoMilk.ChangeDutyCycle(5)
time.sleep(milkAmount)  # 3,7 for 1/4 lap
servoMilk.stop()

#except KeyboardInterrupt:
#  servoMilk.stop()
#  GPIO.cleanup()

servoPlate.start(0) # Initialization
#try:
servoPlate.ChangeDutyCycle(5)
    #time.sleep(plateFinal)
time.sleep(3.7*(4-(mugNr-1)))
    
#except KeyboardInterrupt:
servoPlate.stop()
  #GPIO.cleanup()

