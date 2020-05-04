
import numpy as np
import matplotlib.pyplot as plt



if __name__ == "__main__":

    # format: [batch sizes [batches (green, yellow counts)]]

    data = [   [(0,0),(1,0),(0,1),(0,0),(0,1)], #10
            [(2,2),(1,1),(0,3),(1,1),(0,1)], #20
            [(0,1),(1,0),(1,0),(1,1),(0,1)], #30
            [(1,2),(1,1),(3,2),(4,0),(1,0)], #40
            [(0,1),(1,1),(4,1),(1,0),(1,3)]  #50
        ]

    # percentage of batches with duplicate by batch size
    print("Percentage of batches with duplicates")
    p_dups = []
    for i in data:
        has_dups = []
        for j in i:
            if j[0] > 0:
                has_dups.append(1)
            else:
                has_dups.append(0)
        p_dups.append(sum(has_dups)/len(has_dups))

    x = np.array(list(range(10, 60, 10)))

    ax = plt.subplot(111)
    ax.bar(x, p_dups, width=5, color='g', align='center', label='count')

    ax.hlines(0.5, 5, 55, colors=['r'], linestyles='dashed', label='threshold')

    plt.title("Percent of Batches with Duplicates")

    plt.xlabel("Batch Size")
    plt.ylabel("Percent")

    plt.legend()
    plt.savefig("dup-perc.png")
    plt.clf()

    # average green / yellow per batch size
    print("Average green / yellow per batch size")
    gas = []
    yas = []
    for i in data:
        ga = sum([j[0] for j in i]) / 5
        ya = sum([j[1] for j in i]) / 5
        gas.append(ga)
        yas.append(ya)
    print(gas)
    print(yas)

    x = np.array(list(range(10, 60, 10)))

    ax = plt.subplot(111)
    ax.bar(x-1.5, gas, width=3, color='g', align='center', label="duplicates")
    ax.bar(x+1.5, yas, width=3, color='r', align='center', label="similar")

    plt.title("Average Duplicate Count per Batch Size")

    plt.xlabel("Batch Size")
    plt.ylabel("Average Count")

    plt.legend()
    plt.savefig("dup-count.png")
    plt.clf()
