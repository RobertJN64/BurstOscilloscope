import matplotlib.pyplot as plt

data = []
labels = []

# cmp1 = input("Log file: ")
# cmp2 = input("Log file: ")

cmps = [('nomos', 'Tracker mA'), ('pcb', 'Tracker w/ PCB mA')]

for cmp, label in cmps:
    with open('Logs/' + cmp + '.txt') as f:
        data.append([])
        labels.append(label)
        for line in f.readlines():
            a, b = line.strip().split(',')
            data[-1].append(float(b))

with open('Logs/' + cmps[0][0] + '.txt') as f:
    data.append([])
    labels.append("Volts")
    for line in f.readlines():
        a, b = line.strip().split(',')
        data[-1].append(float(a))

for d, l in zip(data, labels):
    plt.plot(d, label=l)
    plt.legend()

plt.show()