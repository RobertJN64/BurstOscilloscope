import matplotlib.pyplot as plt

data = []
data_2 = []

with open('log_multi.txt') as f:
    for line in f.readlines():
        a, b = line.strip().split(',')
        data.append(float(a))
        data_2.append(float(b))

plt.plot(data)
plt.plot(data_2)
plt.show()