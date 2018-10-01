import wiringpi

def main():
    motor1 = 18
    motor2 = 13
    motor3 = 111  # need to set
    motor4 = 111  # need to set

    #setup wiringpi and pwm ouputs
    wiringpi.wiringPiSetup()

    wiringpi.pinMode(motor1, 2)
    wiringpi.pinMode(motor2, 2)

    wiringpi.pinMode(motor3, 0)
    wiringpi.pinMode(motor4, 0)
    wiringpi.softPwmCreate(motor3, 0, 100)
    wiringpi.softPwmCreate(motor4, 0, 100)


    #0 to 100 range?
    wiringpi.pwmWrite(motor1, 0)
    wiringpi.pwmWrite(motor2, 0)
    wiringpi.softPwmWrite(motor3, 0)
    wiringpi.softPwmWrite(motor4, 0)




if __name__ == "__main__":
    main()