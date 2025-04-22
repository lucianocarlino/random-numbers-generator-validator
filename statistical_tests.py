import math

def mean_test(test: list[float], za: float):
    mean = sum(test) / len(test)
    zo = ((mean - 0.5) * math.sqrt(len(test))) / math.sqrt(1 / 12)
    return {
        "estado": 1,
        "mensaje": "",
        "resultado": abs(zo) < za
    }

def frecuency_test(test: list[float], subintervals: int, chi_squared_a: float):
    ef = len(test) / subintervals
    fo = [0] * subintervals
    for i in range(subintervals):
        fo[i] = sum(1 for _ in filter(lambda x: (1 / subintervals) * i <= x < (1 / subintervals) * (i + 1), test))
    chi_squared = (subintervals / len(test)) * sum([(x - ef) ** 2 for x in fo])
    return{
        "estado": 1,
        "mensaje": "",
        "resultado": chi_squared < chi_squared_a
    }

def series_test(test: list[int], sub_cells: int, chi_squared_a: float):
    ef = (len(test) / 2) / (sub_cells ** 2)
    fo = [0] * (sub_cells ** 2)
    series = list(map(list, zip(test[::2], test[1::2])))
    for i in range(sub_cells):
        for j in range(sub_cells):
            fo[i * sub_cells + j] = sum(1 for _ in filter(lambda x: (1 / sub_cells) * i <= x[0] < (1 / sub_cells) * (i + 1) and (1 / sub_cells) * j <= x[1] < (1 / sub_cells) * (j + 1), series))
    chi_squared = ((sub_cells ** 2) / (len(test) / 2)) * sum([(x - ef) ** 2 for x in fo])
    return {
        "estado": 1,
        "mensaje": "",
        "resultado": chi_squared < chi_squared_a
    }

def ks_test(test: list[int], dan: int):
    sample = test
    sample.sort()
    sample = list(map(lambda x: (x[0] + 1) / len(sample) - x[1], enumerate(sample)))
    d = max(sample)
    return {
        "estado": 1,
        "mensaje": "",
        "resultado": d < dan
    }

def mean_up_and_down_test(test: list[int], chi_squared_an2: float):
    s1 = [] 
    fo = [0] * len(test)
    fe = []
    run = 0
    for number in test:
        if number > 0.5:
            s1.append(1)
        else:
            s1.append(0)
    for i in range(len(s1)):
        if i == len(s1) - 1:
            if s1[i] == s1[i - 1]:
                run += 1
                fo[run] += 1
            else:
                fo[run] += 1
                run = 0
        else:
            if s1[i] == s1[i + 1]:
                run += 1
            else:
                fo[run] += 1
                run = 0
    while fo[-1] == 0:
        fo.pop()
    for i in range(len(fo)):
        fe.append((len(test) - (i + 1) + 3)/math.pow(2, (i + 1) + 1))
    chi_squared= sum([(((fo[i] - fe[i]) ** 2) / fe[i]) for i in range(len(fo))])
    return {
        "estado": 1,
        "mensaje": "",
        "resultado": chi_squared < chi_squared_an2
    }

print(f"Prueba de los promedios {mean_test([0.01, 0.079, 0.168, 0.858, 0.901, 0.74, 0.713, 0.478, 0.277, 0.019, 0.548, 0.426], 0.957)}")
print(f"Prueba de frecuencia {frecuency_test([0.01, 0.079, 0.168, 0.858, 0.901, 0.74, 0.713, 0.478, 0.277, 0.019, 0.548, 0.426], 3, 0.65)}")
print(f"Prueba de series {series_test([0.01, 0.079, 0.168, 0.858, 0.901, 0.74, 0.713, 0.478, 0.277, 0.019, 0.548, 0.426], 2, 0.675)}")
print(f"Prueba de Kolmogorov-Smirnov {ks_test([0.01, 0.079, 0.168, 0.858, 0.901, 0.74, 0.713, 0.478, 0.277, 0.019, 0.548, 0.426], 0.375)}")
print(f"Prueba de up and down {mean_up_and_down_test([0.01, 0.079, 0.168, 0.858, 0.901, 0.74, 0.713, 0.478, 0.277, 0.019, 0.548, 0.426], 7.81)}")