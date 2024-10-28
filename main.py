import network
import ntptime
import time
from Servo import Servo
import ujson


fp = open('secrets.json')
secretsString = fp.read()
secrets = ujson.loads(secretsString)

def dstTime():
    year = time.localtime()[0] #get current year
    # print(year)
    HHMarch = time.mktime((year,3 ,(14-(int(5*year/4+1))%7),1,0,0,0,0,0)) #Time of March change to DST
    HHNovember = time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)) #Time of November change to EST
    # print(HHNovember)
    now=time.time()
    if now < HHMarch : # we are before last sunday of march
        dst=time.localtime(now-18000) # EST: UTC-5H
    elif now < HHNovember : # we are before last sunday of october
        dst=time.localtime(now-14400) # DST: UTC-4H
    else: # we are after last sunday of october
        dst=time.localtime(now-18000) # EST: UTC-5H
    return(dst)


s = network.WLAN(network.STA_IF)
s.active(True)
s.disconnect()
print("Scanned: ", s.scan())
s.connect(secrets['wifi']['ssid'], secrets['wifi']['password']) # Connect to an AP
print("Connected: ", s.isconnected())

while not s.isconnected():
    time.sleep(5)
    print("checking is connected: ", s.isconnected()," ",s.status())
    
if s.isconnected():
    ntptime.settime()

print(time.localtime()," vs ",dstTime())
myDstTime = dstTime()
minutesMotor = Servo(pin=25)
tensMinutesMotor = Servo(pin=26)
hoursMotor = Servo(pin=27)
tensHoursMotor = Servo(pin=15)

ticksPerNumber = 20
while True:
    myDstTime = dstTime()
    totalMinutes=myDstTime[4]
    totalHours=myDstTime[3]

    minutes=totalMinutes % 10
    tensMinutes= (totalMinutes - minutes)/10

    if totalHours == 0 or totalHours == 12:
        tensHours = 1
        hours = 2
    elif totalHours < 12:
        tensHours = totalHours // 10
        hours = totalHours % 10
    else:
        tensHours = 0
        hours = totalHours - 12 

    #print(f"hours: {hours}, totalHours: {totalHours}, tensHours: {tensHours}")
    
    print ("tensHours: ", tensHours, "hours: ",hours," TensMinutes: ", tensMinutes," Minutes: ",minutes)

    minutesAdjustment = 0
    if minutes == 1 or minutes == 2:
        minutesAdjustment = 4
    minutesMotor.move(minutes * ticksPerNumber + minutesAdjustment)
    
    tensMinutesAdjustment = -10   
   
    tensMinutesMotor.move(tensMinutes * ticksPerNumber + tensMinutesAdjustment)
   
    hoursAdjustment = 0
    hoursMotor.move(hours * ticksPerNumber + hoursAdjustment)

    tensHoursAdjustment = 0
    tensHoursMotor.move(tensHours * ticksPerNumber + tensHoursAdjustment)

    time.sleep(1)
