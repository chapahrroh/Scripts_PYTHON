import serial


com_serial = serial.Serial('/dev/ttyS0')
print(com_serial)
com_serial.write(b'12345678')
respuesta= com_serial.readline(5)

print(respuesta)
com_serial.close()
