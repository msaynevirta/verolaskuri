import verolaskuri
import csv
import matplotlib.pyplot as plt

def loop():
    with open("himmeli.csv", 'a') as file:
        for i in range(7500, 20000):
            netto, asumistuki, opintotuki, verot = verolaskuri.ExternalRun(i, 241.50, 500)
            file.write("{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}\n".format(i,netto, asumistuki, opintotuki, verot))

def MPL():
    data = [[],[],[],[],[],[]]
    with open("himmeli.csv", 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        i = 0
        for row in csv_reader:
            if(i != 0):
                data[0].append(i+1)
                data[1].append(float(row[0]))
                data[2].append(float(row[1]))
                data[3].append(float(row[2]))
                data[4].append(float(row[3]))
                data[5].append(float(row[4]))
            i += 1

    plt.figure(figsize=(8,4.84))
    plt.plot(data[1], data[2], linewidth=3)
    plt.plot(data[1], data[3], linewidth=3)
    plt.plot(data[1], data[4], linewidth=3)
    plt.plot(data[1], data[5], linewidth=3)
    plt.show()

def main():
    mode = input("Mode: ")
    if(mode=='l'):
        loop()
    elif(mode=='m'):
        MPL()

main()
