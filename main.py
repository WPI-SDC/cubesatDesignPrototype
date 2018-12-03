import wiringpi
import time

def main():
    # 0 - 1 range
    motor1 = 1
    motor2 = 24
    motor3 = 4
    motor4 = 5

    motor1dir = 21
    motor2dir = 22
    motor3dir = 23
    motor4dir = 25

    wiringpi.wiringPiSetup()
    setupPWM(motor1, motor2, motor3, motor4)
    setupDir(motor1dir, motor2dir, motor3dir, motor4dir)
    print("setup done")
    print("testing motor output")
    speed = 0.6
    print("Running at speed: " + str(speed))
    try:
        while(1):
            writeMotor(motor1, speed, motor1dir, 1)
            writeMotor(motor2, speed, motor2dir, 1)
            writeMotorSoft(motor3, speed, motor3dir, 1)
            writeMotorSoft(motor4, speed, motor4dir, 1)
    except KeyboardInterrupt:
        writeMotor(motor1, 1.0, motor1dir, 1)
        writeMotor(motor2, 1.0, motor2dir, 1)
        print("\nterminating")

def setupPWM(motor1, motor2, motor3, motor4):

    # setup wiringpi and pwm outputs
    wiringpi.wiringPiSetup()

    wiringpi.pinMode(motor1, 2)
    wiringpi.pinMode(motor2, 2)

    wiringpi.pinMode(motor3, 1)
    wiringpi.pinMode(motor4, 1)

    wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
    wiringpi.pwmSetClock(2)
    wiringpi.pwmSetRange(1000)
    
    wiringpi.softPwmCreate(motor3, 0, 100)
    wiringpi.softPwmCreate(motor4, 0, 100)

    wiringpi.pwmWrite(motor1, 0)
    wiringpi.pwmWrite(motor2, 0)
    wiringpi.softPwmWrite(motor3, 100)
    wiringpi.softPwmWrite(motor4, 100)

def setupDir(motor1dir, motor2dir, motor3dir, motor4dir):
    wiringpi.pinMode(motor1dir, 1)
    wiringpi.pinMode(motor2dir, 1)
    wiringpi.pinMode(motor3dir, 1)
    wiringpi.pinMode(motor4dir, 1)

def writeMotor(motor, output, motorDir, outputDir):

    output = output * 1023
    
    if (output >= 0) and (output <= 1023):
        wiringpi.pwmWrite(motor, int(output))
        if(outputDir == 1):
            pass
            #wiringpi.digitalWrite(motorDir, 1)
        elif(outputDir == -1):
            pass
            #wiringpi.digitalWrite(motorDir, 0)
        else:
            print("incorrect direction inputted")

def writeMotorSoft(motor, output, motorDir, outputDir):

    output = output * 100
    
    if (output >= 0) and (output <= 100):
        wiringpi.softPwmWrite(motor, int(output))
        if(outputDir == 1):
            pass
            #wiringpi.digitalWrite(motorDir, 1)
        elif(outputDir == -1):
            pass
            #wiringpi.digitalWrite(motorDir, 0)


if __name__ == "__main__":
    main()
