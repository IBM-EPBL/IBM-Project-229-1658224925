import random
def alarm():
    #print("----------------------------")
    print(" Alert! Temperature is High ")
    #print("----------------------------")
    
def display(temp, hum):
    print("Temperature : ", temp)
    print("Humidity : ", hum)

hum = random.randint(0, 100)
temp = random.randint(0, 100)
if temp > 35:
    alarm()
    display(temp, hum)
else:
    display(temp, hum)
