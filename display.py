import matplotlib.pyplot as plt

data = []

with open('log.txt') as f:
    for line in f.readlines():
        data.append(int(line.strip()))

plt.plot(data)
plt.show()