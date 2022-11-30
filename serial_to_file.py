import serial

port = 'COM8'

fname = input("Enter a filename and press enter to activate the serial dump: ")
scope = serial.Serial(port, 115200)

with open(fname + ".txt", "wb+") as f:
    while True:
        line = scope.readline()
        f.write(line)
        print(line)
        try:
            line = line.decode()
            if "END_SERIAL_LOG" in line:
                break
        except (Exception, ):
            pass
