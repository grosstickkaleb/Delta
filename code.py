        #!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
def callback(channel):
        if GPIO.input(channel):
                print ("No Water Detected!")
        else:
                print ("Water Detected!")
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        time.sleep(1)
        
        
        import tkinter
        from time import strftime

        while True:
            clock_frame = tkinter.Label()
            clock_frame['text'] = '19:12:09'
            clock_frame.pack()

            clock_frame['text'] = '19:38:00'

            current_time = strftime("%H:%M:%S")
            print (current_time)
    
            def tic():
                clock_frame['text'] = strftime("%H:%M:%S")
                def tac():
                    tic()
                    clock_frame.after(100, tac)
