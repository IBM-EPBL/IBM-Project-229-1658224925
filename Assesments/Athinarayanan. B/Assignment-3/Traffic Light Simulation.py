from gpiozero import TrafficLights    
from time import sleep    

lights = TrafficLights(10, 9, 11)    
    
while True:    
           light.green.on()    
           sleep(1)    
           lights.amber.on()    
           sleep(1)    
           lights.red.on()    
           sleep(1) 
