data = []
with open('train_output', 'r', encoding='utf-8') as file:
    for i in file:
        data.append(i)
mile = int(input("input the mileage: "))
print("PREDICTION: ", f'{float(data[0].split(":")[1]) + float(data[1].split(":")[1]) * mile}')