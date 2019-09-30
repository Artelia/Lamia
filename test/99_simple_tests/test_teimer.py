import threading, os, time
delay_time = 2   # delay time in seconds

def watchdog():
  print('Watchdog expired. Exiting...')


alarm = threading.Timer(delay_time, watchdog)

print(type(alarm))
print(isinstance(alarm, threading._Timer))
alarm.start()


time.sleep (1)
print('okok')
"""
if  alarm.isAlive():
    #alarm.cancel()
    del alarm
"""

alarm = threading.Timer(delay_time, watchdog)
alarm.start()

time.sleep (3)

if not alarm.isAlive():
    alarm.start()

time.sleep (3)

alarm.cancel()