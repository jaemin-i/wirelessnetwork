import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

board.digital[7].mode = pyfirmata.OUTPUT

while 1:
    board.digital[7].write(1)
    time.sleep(1)

    board.digital[7].write(0)
    time.sleep(1)
