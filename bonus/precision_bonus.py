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

d = []
with open('.train_output', 'r', encoding='utf-8') as file:
    for i in file:
        d.append(i)

theta0 = float(d[0].split(":")[1])
theta1 = float(d[1].split(":")[1])

n = len(miles)
moy = sum(prices) / n
mae, org, org1 = 0, 0, 0
for i in range(n):
    prediction_i = theta0 + theta1 * miles[i]
    org += (prediction_i - prices[i]) ** 2
    org1 += (prices[i] - moy) ** 2
    mae += abs(prices[i] - prediction_i)

r2 = 1 - (org / org1)
mae = mae / n
print(f"On average, you're off by : {round(mae, 2)} Prices")
print(f"The algo is better at : {round(r2 * 100, 2)}%")
