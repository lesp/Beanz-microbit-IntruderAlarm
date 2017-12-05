from microbit import *
import speech
while True:
    light = pin1.read_analog()
    if light < 1015:
        print("ALERT")
        speech.say("INTRUDER ALERT", speed=120, pitch=100, throat=100, mouth=200)
        sleep(1000)
    else:
        sleep(100)
    
