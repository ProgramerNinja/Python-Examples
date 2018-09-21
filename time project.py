##jared mcmahon
##9-21-18

import time
import calendar

def clock():
    total_seconds = calendar.timegm(time.gmtime())
    calendar.timegm(time.gmtime())

    current_second = total_seconds %60
    
    total_minutes = total_seconds // 60
    
    current_minute = total_minutes % 60

    total_hours = total_minutes // 60

    current_hour = total_hours % 60

    current_hour = current_hour - 6


    print(current_hour , ":" , current_minute , ":" , current_second)

clock()

i=1
while i==1:
    clock()
    time.sleep(1)
