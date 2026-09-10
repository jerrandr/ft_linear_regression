import csv
import sys
miles, prices = [], []
try:
	with open('data.csv', 'r', encoding='utf-8') as data:
		for i in csv.DictReader(data):
			if len(i) != 2:
				raise ValueError
			miles.append(float(i['km']))
			prices.append(float(i['price']))
except (FileNotFoundError, PermissionError, ValueError, TypeError, KeyError):
	print("There was an error on the file or file doesn't exist")
	sys.exit()

if max(miles) == min(miles):
	print("All the miles are the same, can't do a linear regression")
	sys.exit()

if len(miles) <= 0 or len(prices) <= 0:
	print("There are no miles or prices data")
	sys.exit()

if len(miles) == 1 or len(prices) == 1:
	print("At least you must have more than one data")
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

for i in range(1000):
	theta0, theta1 = theta0 - Get_tmp0(), theta1 - Get_tmp1()

real_theta1 = theta1 / (max(miles) - min(miles))
real_theta0 = theta0 - theta1 * min(miles) / (max(miles) - min(miles))

try:
	with open('.train_output', 'w', encoding='utf-8') as f:
		f.write(f'theta0:{real_theta0}\ntheta1:{real_theta1}')
except (FileNotFoundError, PermissionError):
	print("There was an error on the file or file doesn't exist")
	sys.exit()