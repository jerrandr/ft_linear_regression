import matplotlib.pyplot as plt
import csv
import sys
d = []
try:
    with open('.train_output', 'r', encoding='utf-8') as file:
        for i in file:
            d.append(i)
except (FileNotFoundError, PermissionError):
    print("There was an error on the file or file doesn't exist")
    sys.exit()

mile = float(input("input the mileage: "))
prediction = float(d[0].split(":")[1]) + float(d[1].split(":")[1]) * mile
print("OUTPUT: ", prediction)

miles, prices = [], []
try:
    with open('data.csv', 'r', encoding='utf-8') as data:
        for i in csv.DictReader(data):
            miles.append(int(i['km']))
            prices.append(int(i['price']))
except (FileNotFoundError, PermissionError):
    print("There was an error on the file or file doesn't exist")
    sys.exit()


def ft_linspace(begin, end, point):
    pas = (end - begin) / (point - 1)
    return [begin + i * pas for i in range(point)]


x = ft_linspace(min(miles), max(miles), 100)
y = [float(d[0].split(":")[1]) + float(d[1].split(":")[1]) * i for i in x]
plt.title("ft_linear_regression")
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(miles, prices, color='red')
plt.plot(x, y)
plt.show()
