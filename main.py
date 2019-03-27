import wiringpi
import time
import sys
import smbus

DEVICE_ADDRESS = 0x68

def main():
    if len(sys.argv) < 5:
        print ("Not enough arguments")
        return -1
    if float(sys.argv[1]) > 1.0 or float(sys.argv[1]) < -1.0:
        print ("Incorrect range")
        return -1
    if float(sys.argv[2]) > 1.0 or float(sys.argv[2]) < -1.0:
        print ("Incorrect range")
        return -1
    if float(sys.argv[3]) > 1.0 or float(sys.argv[3]) < -1.0:
        print ("Incorrect range")
        return -1
    if float(sys.argv[4]) > 1.0 or float(sys.argv[4]) < -1.0:
        print ("Incorrect range")
        return -1
    # 0 - 1 range
    motor11 = 27
    motor12 = 28
    motor21 = 4
    motor22 = 5
    motor31 = 21
    motor32 = 22
    motor41 = 23
    motor42 = 25

    wiringpi.wiringPiSetup()
    bus = smbus.SMBus(1)
    setupPWM(motor11, motor12, motor21, motor22, motor31, motor32, motor41, motor42)
    #setupDir(motor1dir, motor2dir, motor3dir, motor4dir)
    print("setup done")
    print("testing motor output")
    try:
        while(1):
            writeMotorSoft(motor21,motor22, float(sys.argv[1]))
            writeMotorSoft(motor31,motor32, float(sys.argv[2]))
            writeMotorSoft(motor41,motor42, float(sys.argv[3]))
            writeMotorSoft(motor11,motor12, float(sys.argv[4]))
            #print("z: %5d" % (getZaxis(bus)))
            print("x: %5d, y: %5d, z: %5d" % (getXaxis(bus), getYaxis(bus), getZaxis(bus)))
            # print("gyro x: " + str(getXaxis(bus)) + " y: " + str(getYaxis(bus)) + " z: " + str(getZaxis(bus)))
            
    except KeyboardInterrupt:
        writeMotorSoft(motor21,motor22, 0)
        writeMotorSoft(motor31,motor32, 0)
        writeMotorSoft(motor41,motor42, 0)
        writeMotorSoft(motor11,motor12, 0)
        print("\nterminating")

def setupPWM(motor11, motor12, motor21, motor22, motor31, motor32, motor41, motor42):

    # setup wiringpi and pwm outputs
    wiringpi.wiringPiSetup()

    wiringpi.pinMode(motor11, 1)
    wiringpi.pinMode(motor12, 1)
    wiringpi.pinMode(motor21, 1)
    wiringpi.pinMode(motor22, 1)
    wiringpi.pinMode(motor31, 1)
    wiringpi.pinMode(motor32, 1)
    wiringpi.pinMode(motor41, 1)
    wiringpi.pinMode(motor42, 1)

    wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
    wiringpi.pwmSetClock(2)
    wiringpi.pwmSetRange(1000)

    wiringpi.softPwmCreate(motor11, 0, 100)
    wiringpi.softPwmCreate(motor12, 0, 100)
    wiringpi.softPwmCreate(motor21, 0, 100)
    wiringpi.softPwmCreate(motor22, 0, 100)
    wiringpi.softPwmCreate(motor31, 0, 100)
    wiringpi.softPwmCreate(motor32, 0, 100)
    wiringpi.softPwmCreate(motor41, 0, 100)
    wiringpi.softPwmCreate(motor42, 0, 100)

    wiringpi.softPwmWrite(motor11, 100)
    wiringpi.softPwmWrite(motor12, 100)
    wiringpi.softPwmWrite(motor21, 100)
    wiringpi.softPwmWrite(motor22, 100)
    wiringpi.softPwmWrite(motor31, 100)
    wiringpi.softPwmWrite(motor32, 100)
    wiringpi.softPwmWrite(motor41, 100)
    wiringpi.softPwmWrite(motor42, 100)


def writeMotorSoft(motorOut1, motorOut2, output):
    outputDir = 1
    if(output < 0):
        outputDir = -1
        output = output * -1

    output = output * 100
    
    if (output >= 0) and (output <= 100):
        if(outputDir == 1):
            wiringpi.softPwmWrite(motorOut1, int(output))
            wiringpi.softPwmWrite(motorOut2, 0) # stop second motor
        elif(outputDir == -1):
            wiringpi.softPwmWrite(motorOut1, 0) # stop first motor
            wiringpi.softPwmWrite(motorOut2, int(output))

def getXaxis(bus):
    high = bus.read_byte_data(DEVICE_ADDRESS,0x43)
    low = bus.read_byte_data(DEVICE_ADDRESS,0x44)

    returnedData = (high * 256 + low) * 131
    return returnedData
    #return (returnedData - 65536) if (returnedData > 32767) else returnedData

def getYaxis(bus):
    high = bus.read_byte_data(DEVICE_ADDRESS,0x45)
    low = bus.read_byte_data(DEVICE_ADDRESS,0x46)

    returnedData = (high * 256 + low) * 131
    return returnedData
    #return (returnedData - 65536) if (returnedData > 32767) else returnedData

def getZaxis(bus):
    high = bus.read_byte_data(DEVICE_ADDRESS,0x47)
    low = bus.read_byte_data(DEVICE_ADDRESS,0x48)

    returnedData = (high * 256 + low) * 131
    return returnedData
    # return (returnedData - 65536) if (returnedData > 32767) else returnedData


if __name__ == "__main__":
    main()
