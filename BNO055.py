import time
import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)

def get_data():

    acce = float('{0:.1f}'.format(sensor.accelerometer))
    gyro = float('{0:.1f}'.format(sensor.gyroscope))
    magn = sensor.magnetometer
    euler = sensor.euler
    quatern = sensor.quaternion
    lin_acc = sensor.linear_acceleration
    grav = sensor.gravity    
    
    try:
        with open('BNO055.csv', 'a') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(
                ["Accelerometer (m/s^2) =", accelerometer, "Magnetism =", magn, "Euler ="sensor.euler, "Quaternion =",quatern,"Linear Acceleration =",lin_acc, "Gravity =", grav, "Gyroscope (deg/sec) = ", gyroscope])
    except:
        pass

    return [accelerometer, gyroscope]

get_data()
