import os
import matplotlib.pyplot as plt

def gen_graph(name, loops, shared):
    if name == 'Branch Miss':
        index = 15
    elif name == 'Branch':
        index = 14
    elif name == 'Instructions Per Cycle':
        index = 12

    loopsData = list()

    for i in range(len(loops)):
        loopsData.append(int(loops[i][index].strip().split(' ')[0].replace(',', '')))

    sharedData = list()

    for i in range(len(shared)):
        sharedData.append(int(shared[i][index].strip().split(' ')[0].replace(',', '')))

    print(loopsData, sharedData)
    plt.figure()
    plt.ylabel(f'{name}')
    plt.xlabel('Loop Iterations')
    plt.xticks(list(range(10)))
    plt.scatter(list(range(10)), loopsData, color='blue')
    plt.scatter(list(range(10)), sharedData, color='red')
    plt.legend(['Loops', 'Large Arrays'])
    plt.savefig(os.path.join(os.getcwd(), 'images', f'{name}.png'))

loops = list()
shared = list()

for file in os.listdir(os.getcwd()):
    if 'loops_stat' in file:
        loop = open(file, 'r')
        data = loop.readlines()
        loops.append(data)
        loop.close()
    elif 'shared_stat' in file:
        share = open(file, 'r')
        data = share.readlines()
        shared.append(data)
        share.close()

gen_graph('Branch Miss', loops, shared)
gen_graph('Branch', loops, shared)
gen_graph('Instructions Per Cycle', loops, shared)