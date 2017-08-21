import smbus
import math

class xSlopeClass:

    # Power management registers
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
    address = 0x68       # This is the address value read via the i2cdetect command

    # Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(address, 0x6b, 0)


    def read_byte(adr):
        return bus.read_byte_data(address, adr)

    def read_word(self,adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self,adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val

    def dist(dist,a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(self,x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)

    def xSlope(self):

        print
        print "accelerometer data"
        print "------------------"

        accel_xout = self.read_word_2c(0x3b)
        accel_yout = self.read_word_2c(0x3d)
        accel_zout = self.read_word_2c(0x3f)

        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0

        print "x rotation: " , self.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

        return self.get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)



    
