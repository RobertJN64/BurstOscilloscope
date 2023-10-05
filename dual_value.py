import serial

port = 'COM9'
length = 1000

scope = serial.Serial(port, 115200)
data = []

while True:
    line = scope.readline().decode('utf-8').strip()
    if '$' in line:
        data.append(line.replace('$:', ''))
        if (len(data) * 100 / length).is_integer():
            print(str(int(len(data) * 100 / length)) + "%")
    elif '#' in line:
        break
    elif '*' in line:
        length = int(line.replace('*',''))
    else:
        print(line)


with open('log_multi.txt', 'w+') as f:
    for line in data:
        f.write(str(line) + '\n')
