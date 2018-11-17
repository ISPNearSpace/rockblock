import CCS811
import BME280
import BNO055

CCS811.save_data()
print BME280.get_data()
print BNO055.get_data()
