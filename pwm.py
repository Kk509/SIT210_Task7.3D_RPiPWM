import RPi.GPIO as GPIO
import time
import numpy as np

#GPIO pins
led = 17
trig = 4
echo = 27

#set GPIO mode
GPIO.setmode(GPIO.BCM)

#setup
GPIO.setup(led, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

#distance and duty range
distance_range = np.array([10, 20, 50, 100])
duty_cycle_range = np.array([100, 50, 25, 0])

#create pwm instance, start pwm at 0 duty cycle
pwm = GPIO.PWM(led, 100)
pwm.start(0)

def distance():

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo)==0:
                pulse_start = time.time()
        while GPIO.input(echo)==1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        return distance

try:
        GPIO.output(trig, GPIO.LOW)
        print ("Waiting for sensor to settle")
        time.sleep(2)

        current_duty_cycle = 0
        while True:
                x = distance()

                duty_cycle = np.interp(x, distance_range, duty_cycle_range)
                step = 1 if duty_cycle > current_duty_cycle else -1
                for i in range(int(current_duty_cycle), int(duty_cycle), step):
                        pwm.ChangeDutyCycle(i)
                        time.sleep(0.01) 
                
		current_duty_cycle = duty_cycle
                print ("distance:", x, "cm")
                time.sleep(0.5)
		
except KeyboardInterrupt:
        GPIO.cleanup()
