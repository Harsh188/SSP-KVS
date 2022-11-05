import os
import matplotlib.pyplot as plt

def gen_graph(name, column, row):
    if 'Cache_Misses' in name:
        index = 4
    elif 'Time_Taken' in name:
        index = 6
    print(index)
    columnData = list()

    for i in range(len(column)):
        columnData.append(float(column[i][index].strip().split(' ')[0].replace(',', '')))

    rowData = list()

    for i in range(len(row)):
        rowData.append(float(row[i][index].strip().split(' ')[0].replace(',', '')))

    print(columnData, rowData)
    dim_list = [100, 500, 1000]

    columnData.sort()
    rowData.sort()
    
    plt.figure()
    plt.ylabel(name)
    plt.xlabel('Array Dimension')
    plt.xticks(dim_list)
    plt.plot(dim_list, columnData, color='blue')
    plt.plot(dim_list, rowData, color='red')
    plt.legend(['Column Traversal', 'Row Traversal'])
    plt.savefig(os.path.join(os.getcwd(), f'{name}.png'))

column = list()
row = list()

for file in os.listdir(os.getcwd()):
    if ".txt" in file:
        if 'ctest_2d' in file:
            loop = open(file, 'r')
            data = loop.readlines()
            column.append(data)
            loop.close()
        elif 'rtest_2d' in file:
            share = open(file, 'r')
            data = share.readlines()
            row.append(data)
            share.close()
gen_graph('Cache_Misses_2d', column, row)
gen_graph('Time_Taken_2d', column, row)

column = list()
row = list()

for file in os.listdir(os.getcwd()):
    if ".txt" in file:
        if 'ctest_3d' in file:
            loop = open(file, 'r')
            data = loop.readlines()
            column.append(data)
            loop.close()
        elif 'rtest_3d' in file:
            share = open(file, 'r')
            data = share.readlines()
            row.append(data)
            share.close()

gen_graph('Cache_Misses_3d', column, row)
gen_graph('Time_Taken_3d', column, row)