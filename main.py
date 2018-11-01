import wiringpi
import time

def main():
    motor1 = 1 # 0-1023
    motor2 = 24 # 0-1023
    motor3 = 28 # 0-100
    motor4 = 29 # 0-100

    wiringpi.wiringPiSetup()
    setup(motor1, motor2, motor3, motor4)
    print("setup done")
    print("testing motor output")
    #writeMotor(motor1, 512)
    writeMotorSoft(motor3, 50)

def setup(motor1, motor2, motor3, motor4):

    # setup wiringpi and pwm outputs
    wiringpi.wiringPiSetup()

    wiringpi.pinMode(motor1, 2)
    wiringpi.pinMode(motor2, 2)

    wiringpi.pinMode(motor3, 1)
    wiringpi.pinMode(motor4, 1)
    wiringpi.softPwmCreate(motor3, 0, 100)
    wiringpi.softPwmCreate(motor4, 0, 100)

    wiringpi.pwmWrite(motor1, 0)
    wiringpi.pwmWrite(motor2, 0)
    wiringpi.softPwmWrite(motor3, 0)
    wiringpi.softPwmWrite(motor4, 0)

def writeMotor(motor, output):

    if (output >= 0) and (output <= 1023):
        wiringpi.softPwmWrite(motor, output)

def writeMotorSoft(motor, output):

    if (output >= 0) and (output <= 100):
        wiringpi.softPwmWrite(motor, output)


if __name__ == "__main__":
    main()
