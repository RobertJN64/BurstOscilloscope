import matplotlib.pyplot as plt

data = []
labels = []

# cmp1 = input("Log file: ")
# cmp2 = input("Log file: ")

cmp1 = 'mosfet'
cmp2 = 'pcb'
cmp3 = 'pcb_1.1'
cmp4 = 'nomos'


for cmp in [cmp1, cmp2, cmp3, cmp4]:
    with open('Logs/' + cmp + '.txt') as f:
        data.append([])
        labels.append(cmp + " mAmps")
        for line in f.readlines():
            a, b = line.strip().split(',')
            data[-1].append(float(b))

with open('Logs/' + cmp1 + '.txt') as f:
    data.append([])
    labels.append("Volts")
    for line in f.readlines():
        a, b = line.strip().split(',')
        data[-1].append(float(a))

for d, l in zip(data, labels):
    plt.plot(d, label=l)
    plt.legend()

plt.show()