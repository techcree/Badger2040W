# Blinky badger fun!
import badger2040w as badger2040
#import badger2040
import time

badger = badger2040.Badger2040W()

count = 0

if count <= 3:
    badger.led(255)
    time.sleep(1)
    badger.led(0)
    time.sleep(0.2)
    
    count = count +1

else:
    pass