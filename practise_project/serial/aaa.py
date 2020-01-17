import serial

ser = serial.Serial('COM1',
                    baudrate = 115200,
                    bytesize = 8,
                    parity = 'N',
                    stopbits = 1)



