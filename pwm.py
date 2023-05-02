import RPi.GPIO as GPIO
import time
ledpin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin, GPIO.OUT)

#create pwm instance with frequency 1000Hz
led_pwm = GPIO.PWM(ledpin, 1000)
#start the pwm at 0 duty cycle
led_pwm.start(0)

try:    
	while True:
		#for loop from 0-100% duty 
		for duty in range(0, 101):
			led_pwm.ChangeDutyCycle(duty)
			#generate delay every 10 millisecond
			time.sleep(0.01)

		time.sleep(0.5)

		#for loop from 100-0% duty
		for duty in range(100, -1, -1):
			led_pwm.ChangeDutyCycle(duty)
			time.sleep(0.01)

		time.sleep(0.5)

except KeyboardInterrupt:
        GPIO.cleanup()
