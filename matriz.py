rows = int(input('Type the quantity: '))


matriz = [[rows]]

for i in matriz:
    for j in i:
        t = [[2, 3, 4], [8, 3, 4]]
        p = [[5, 10, 6], [10, 4, 7]]
        print(matriz[t][p])
        
for k in matriz:
    for t in matriz:
        print("line: {} | column {}".format(k, t))