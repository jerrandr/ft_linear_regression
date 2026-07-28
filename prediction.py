d = []
with open('.train_output', 'r', encoding='utf-8') as file:
    for i in file:
        d.append(i)
mile = float(input("input the mileage: "))
print("PREDICTION: ", f'{float(d[0].split(":")[1]) + float(d[1].split(":")[1]) * mile}')
