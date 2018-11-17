import time
import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)

def get_data():

    def accRead(): #m/s^2
        acce = float('{0:.1f}'.format(sensor.accelerometer))
        return acce

    def gyroRead(): #deg/sec
        gyro = float('{0:.1f}'.format(sensor.gyroscope))
        return gyro

    accelerometer = float(accRead())
    gyroscope = float(gyroRead())

    try:
        with open('BNO055.csv', 'a') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(
                ["Accelerometer (m/s^2) =", accelerometer, "Gyroscope (deg/sec) = ", gyroscope])
    except:
        pass

    return [accelerometer, gyroscope]