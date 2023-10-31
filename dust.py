import serial

cmd = 'temp'

seri = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = None)
seri.write(cmd.encode())
print(seri.name)

a = 1
while a:
    if seri.in_waiting != 0:
        content =seri.readline()
        print(content.decode())
        a = 0
