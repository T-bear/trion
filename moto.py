import RPi.GPIO as GPIO
import time

#Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

#Set up pins for different servos 
servoPIN1 = 17
#servoPIN2 = 1337 #Choose appropriate PIN
#servoPIN3 = 1337 #Choose appropriate PIN


GPIO.setup(servoPIN1, GPIO.OUT)
servoCoffee = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
GPIO.setup(servoPIN2, GPIO.OUT)
servoMilk = GPIO.PWM(servoPIN2, 50) # GPIO 1337 for PWM with 50Hz
GPIO.setup(servoPIN2, GPIO.OUT)
servoPlate = GPIO.PWM(servoPIN3, 50) # GPIO 1337 for PWM with 50Hz

svar = False  ######### Choose milk amount ###########
while svar == False:

  milkAmount = 1
  milkAmount = int(input("How much milk? (Must be between 0 - 10)" ))
  if(milkAmount < 0 or milkAmount > 10):
    print("Svar ej giltigt.")

  else: 
    svar = True 

svar2 = False  ######### Choose coffr amount ###########
while svar2 == False:

  coffeeAmount = int(input("Hur starkt kaffe vill du ha? (Svar måste vara mellan 0 - 10)" ) ) 
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

if(mugNr == 1): plateFinal = 0
elif (mugNr == 2):plateFinal = 90
elif (mugNr == 3):plateFinal = 180
elif (mugNr == 4):plateFinal = 270


coffeeFinal = stdValueCoffee * (coffeeAmount / 100) ##justeras div grejjor

milkFinal = stdValueMilk * (milkAmount / 100)  ##justeras div grejjor



print("Du valde milkamount: " , milkAmount)
print("Du valde coffeamount: " , coffeeAmount)
print("Du valde mugg: " , mugNr)


#servoPlate.start(2.5) # Initialization
#try:
#  while True:
#    servoPlate.ChangeDutyCycle(plate)
#    time.sleep(plateFinal)  
#    
#except KeyboardInterrupt:
#  servoPlate.stop()
#  GPIO.cleanup()

servoCoffee.start(2.5) # Initialization
try:
  while True:
    servoCoffee.ChangeDutyCycle(5)
    time.sleep(coffeeFinal)   
    
except KeyboardInterrupt:
  servoCoffee.stop()
  GPIO.cleanup()

#servoMilk.start(2.5) # Initialization
#try:
#  while True:
#    servoMilk.ChangeDutyCycle(5)
#    time.sleep(milkFinal)   
#    
#except KeyboardInterrupt:
#  servoMilk.stop()
#  GPIO.cleanup()


