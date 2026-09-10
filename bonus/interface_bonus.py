import matplotlib.pyplot as plt
import csv
import sys

miles, prices = [], []
try:
    with open('data.csv', 'r', encoding='utf-8') as data:
        for i in csv.DictReader(data):
            miles.append(int(i['km']))
            prices.append(int(i['price']))
except (FileNotFoundError, PermissionError):
    print("There was an error on the file or file doesn't exist")
    sys.exit()

m, theta0, theta1 = len(miles), 0.0, 0.0
miles_norm = [(x - min(miles)) / (max(miles) - min(miles)) for x in miles]


def estimatePrice(x):
    return theta1 * x + theta0


def Get_tmp0():
    tmp0 = 0.0
    for i in range(m):
        tmp0 += estimatePrice(miles_norm[i]) - prices[i]
    return tmp0 * 0.1 / m


def Get_tmp1():
    tmp1 = 0.0
    for i in range(m):
        tmp1 += (estimatePrice(miles_norm[i]) - prices[i]) * miles_norm[i]
    return tmp1 * 0.1 / m

def ft_linspace(begin, end, point):
    pas = (end - begin) / (point - 1)
    return [begin + i * pas for i in range(point)]

for i in range(1000):
    theta0, theta1 = theta0 - Get_tmp0(), theta1 - Get_tmp1()

real_theta1 = theta1 / (max(miles) - min(miles))
real_theta0 = theta0 - theta1 * min(miles) / (max(miles) - min(miles))

d = [f"theta0:{real_theta0}", f"theta1:{real_theta1}"]


x = ft_linspace(min(miles), max(miles), 100)
y = [float(d[0].split(":")[1]) + float(d[1].split(":")[1]) * i for i in x]

plt.title("ft_linear_regression")
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(miles, prices, color='red')
plt.plot(x, y)
plt.show()
