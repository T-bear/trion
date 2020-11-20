import RPi.GPIO as GPIO
import time

#Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

#Set up pins for different servos 
servoPIN1 = 17
servoPIN2 = 1337 #Här skrivs lämplig pin in
servoPIN3 = 1337 #Här skrivs lämplig pin in


GPIO.setup(servoPIN1, GPIO.OUT)
servoCoffee = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
GPIO.setup(servoPIN2, GPIO.OUT)
servoMilk = GPIO.PWM(servoPIN2, 50) # GPIO 1337 for PWM with 50Hz
GPIO.setup(servoPIN2, GPIO.OUT)
servoPlate = GPIO.PWM(servoPIN3, 50) # GPIO 1337 for PWM with 50Hz

svar = False  ######### Här väljer man sin mjölk mängd som mann vill ha ###########
while svar == False:

  #Tänker att standard mängden blir svag och att man väljer att öka respektive med upp till 10%
  milkAmount = 1
  milkAmount = int(input("Hur mycket mjölk vill du ha? (Svar måste vara mellan 0 - 10)" ))
  if(milkAmount < 0 or milkAmount > 10):
    print("Svar ej giltigt.")

  else: 
    svar = True 

svar2 = False  ######### Här väljer man sin kaffe mängd som mann vill ha ###########
while svar2 == False:

  # Tänker att standard mängd blir 5 och att man väljer att öka respektive sänka med 5% + att 0 exkluderar helt

  coffeeAmount = int(input("Hur starkt kaffe vill du ha? (Svar måste vara mellan 0 - 10)" ) ) 
  if(coffeeAmount < 0 or coffeeAmount > 10):
    print("Svar ej giltigt.")

  else: 
    svar2 = True 

svar3 = False   ######### Här väljer man sin mugg ###########
while svar3 == False:
  mugNr = int(input("Välj din mugg! (Svar måste vara 1, 2, 3 eller 4)"))   
  if(mugNr < 1 or mugNr > 4):
    print("Svar ej giltigt.")

  else:
    svar3 = True

#### Här tänkte jag fixa så att de första frågorna faktiskt justerar något

#Standardvärde för samtliga saker

stdValueCoffee = 5
stdValueMilk = 5
stdValuePlate = 0

if(mugNr == 1): plateFinal = 0
elif (mugNr == 2):plateFinal = 90
elif (mugNr == 3):plateFinal = 180
elif (mugNr == 4):plateFinal = 270


coffeeFinal = stdValueCoffee * (coffeeAmount / 100) ##Här justeras div grejjor

milkFinal = stdValueMilk * (milkAmount / 100)  ##Här justeras div grejjor



print("Du valde mjölkmängd: " , milkAmount)
print("Du valde kaffemängd: " , coffeeAmount)
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

#servoCoffee.start(2.5) # Initialization
#try:
#  while True:
#    servoCoffee.ChangeDutyCycle(5)
#    time.sleep(coffeeFinal)   
#    
#except KeyboardInterrupt:
#  servoCoffee.stop()
#  GPIO.cleanup()

#servoMilk.start(2.5) # Initialization
#try:
#  while True:
#    servoMilk.ChangeDutyCycle(5)
#    time.sleep(milkFinal)   
#    
#except KeyboardInterrupt:
#  servoMilk.stop()
#  GPIO.cleanup()


