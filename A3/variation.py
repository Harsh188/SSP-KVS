import os
import matplotlib.pyplot as plt

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

bmiss_loops = list()

for i in range(len(loops)):
    bmiss_loops.append(int(loops[i][15].strip().split(' ')[0].replace(',', '')))

bmiss_shared = list()

for i in range(len(shared)):
    bmiss_shared.append(int(shared[i][15].strip().split(' ')[0].replace(',', '')))


plt.ylabel('Branch Misses')
plt.xlabel('Loop Iterations')
plt.xticks(list(range(10)))
plt.scatter(list(range(10)), bmiss_loops, color='blue')
plt.scatter(list(range(10)), bmiss_shared, color='red')
plt.legend(['Loops', 'Large Arrays'])
plt.savefig(os.path.join(os.getcwd(), 'images', 'branch miss.png'))