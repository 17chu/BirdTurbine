from pyfirmata import Arduino, util
import time


board = Arduino("COM5")
iterator = util.Iterator(board)
iterator.start()
count = 0
Buzzer = board.get_pin('d:3:p')

#Buzzer.write(0)
#time.sleep(1.0)
for i in range(100):
    for i in range(128):
        Buzzer.write(i)
        #Buzzer.write(0)
        count+=1
        print(i)
    
Buzzer.write(0)    
    
 
#Buzzer.write(100)
#print(count)   
#time.sleep(3.0)
#count+=1
#Buzzer.write(0)

print(str(count) + str("hello"))
board.exit()

