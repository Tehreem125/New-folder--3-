# make countdown timer

import time #import time module


seconds = int(input("Please enter the number of seconds: "))
def countdown(seconds):
    """this function will take time as input"""
    while seconds>0:
        mins, secs = divmod(seconds , 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
       
        print(timer)
        time.sleep(1) # wait for 1 second
        seconds -= 1
    print("Time's up") #when countdown is equal to zero
        
countdown(seconds)