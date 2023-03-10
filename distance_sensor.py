#!/usr/bin/python
import RPi.GPIO as GPIO
import time

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    while(True):
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        # Waiting for sensor to settle
        time.sleep(2)

        print("Reading at:" + time.asctime())
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            pass
        pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pass
        pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = round(pulse_duration * 17150, 2)
        print("Distance: ",distance, " cm")
finally:
    GPIO.cleanup()