from Servo import Servo
import time

print(time.localtime())
motor = Servo(pin=25)
ticksPerNumber = 20
while True:
    totalMinutes=time.localtime()[4]
    print ("Total Minutes: ",totalMinutes)
    minutes=totalMinutes % 10
    print ("Minutes: ",minutes)
    tensMinutes=totalMinutes - minutes

    adjustment = 0
    if minutes == 1 or minutes == 2:
        adjustment = 4
    motor.move( minutes * ticksPerNumber + adjustment)
    time.sleep(1)
    
    
# motor = Servo(pin=25)
# ticksPerNumber = 20
# motor.move(0 * ticksPerNumber)
# time.sleep(1)
# motor.move(1 * ticksPerNumber + 4)
# time.sleep(1)
# motor.move(2 * ticksPerNumber + 4)
# time.sleep(1)
# motor.move(3 * ticksPerNumber)
# time.sleep(1)
# motor.move(4 * ticksPerNumber)
# time.sleep(1)
# motor.move(5 * ticksPerNumber)
# time.sleep(1)
# motor.move(6 * ticksPerNumber)
# time.sleep(1)
# motor.move(7 * ticksPerNumber)
# time.sleep(1)
# motor.move(8 * ticksPerNumber)
# time.sleep(1)
# motor.move(9 * ticksPerNumber)
# time.sleep(1)
# motor.move(0)
# time.sleep(1)
