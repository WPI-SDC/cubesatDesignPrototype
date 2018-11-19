import wiringpi
import time

def main():
    # 0 - 1 range
    motor1 = 1
    motor2 = 24
    motor3 = 4
    motor4 = 5

    wiringpi.wiringPiSetup()
    setup(motor1, motor2, motor3, motor4)
    print("setup done")
    print("testing motor output")

    try:
        while(1):
            writeMotor(motor1, 0.68)
            writeMotor(motor2, 0.68)
            writeMotorSoft(motor3, 0.68)
            writeMotorSoft(motor4, 0.68)
    except KeyboardInterrupt:
        print("exiting")

def setup(motor1, motor2, motor3, motor4):

    # setup wiringpi and pwm outputs
    wiringpi.wiringPiSetup()

    wiringpi.pinMode(motor1, 2)
    wiringpi.pinMode(motor2, 2)

    wiringpi.pinMode(motor3, 1)
    wiringpi.pinMode(motor4, 1)

    wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
    
    wiringpi.softPwmCreate(motor3, 0, 100)
    wiringpi.softPwmCreate(motor4, 0, 100)

    wiringpi.pwmWrite(motor1, 0)
    wiringpi.pwmWrite(motor2, 0)
    wiringpi.softPwmWrite(motor3, 100)
    wiringpi.softPwmWrite(motor4, 100)

def writeMotor(motor, output):

    output = output * 1023
    
    if (output >= 0) and (output <= 1023):
        wiringpi.pwmWrite(motor, int(output))

def writeMotorSoft(motor, output):

    output = output * 100
    
    if (output >= 0) and (output <= 100):
        wiringpi.softPwmWrite(motor, int(output))


if __name__ == "__main__":
    main()
