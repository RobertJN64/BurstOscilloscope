import serial

port = 'COM5'
length = 0

scope = serial.Serial(port, 115200)
data = []

while True:
    line = scope.readline().decode('utf-8').strip()
    if '$' in line:
        data.append(int(line.replace('$:', '')))
        if (len(data) * 100 / length).is_integer():
            print(str(int(len(data) * 100 / length)) + "%")
    elif '#' in line:
        break
    elif '*' in line:
        length = int(line.replace('*',''))
    else:
        print(line)


with open('log.txt', 'w+') as f:
    for line in data:
        f.write(str(line) + '\n')
