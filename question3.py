import json

def main():
    with open("dados.json", "r") as fp:
        data = json.load(fp)
    
    mean = 0
    total_days = 0
    min_value = float('inf')  # maior valor para comecar
    max_value = 0

    for x in data:
        value = x["valor"]

        if value != 0:
            mean += value
            total_days += 1
            if min_value > value:
                min_value = value
            if max_value < value:
                max_value = value

    mean = mean/total_days

    above_average_days = 0
    for x in data:
        value = x["valor"]
        if value > mean:
            above_average_days += 1

    print(f"Menor valor de faturamento: {min_value}")
    print(f"Maior valor de faturamento: {max_value}")
    print(f"Dias melhores que a média: {above_average_days}")



if __name__ == '__main__':
    main()