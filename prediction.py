import sys
d = []
try:
    with open('.train_output', 'r', encoding='utf-8') as file:
        for i in file:
            d.append(i)
except (FileNotFoundError, PermissionError):
    print("PREDICTION: 0")
    sys.exit()
mile = float(input("input the mileage: "))
a, b = float(d[0].split(":")[1]), float(d[1].split(":")[1])
print("PREDICTION: ", f'{a + b * mile}')
