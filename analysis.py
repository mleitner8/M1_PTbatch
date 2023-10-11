"""
analysis.py

Functions to read and plot figures from the batch stimulation results
"""

import utils
import json
import matplotlib.pyplot as plt


def plotFI(dataFolder, batchLabel, params, data):
    utils.setPlotFormat(numColors = 8)
    Pvals = params[0]['values']
    Ivals = params[1]['values']

    Pvalsdic = {val: i for i, val in enumerate(Pvals)}
    Ivalsdic = {val: i for i, val in enumerate(Ivals)}

    rates = [[0 for x in range(len(Pvals))] for y in range(len(Ivals))]
    for key, d in data.items():
        rate = len(d['simData']['spkt'])
        Pindex = Pvalsdic[d['paramValues'][0]]
        Iindex = Ivalsdic[d['paramValues'][1]]
        rates[Iindex][Pindex] = rate
        print(d['paramValues'])
        print(rate)

    filename = '%s/%s/%s_fIcurve.json' % (dataFolder, batchLabel, batchLabel)
    with open(filename, 'w') as fileObj:
        json.dump(rates, fileObj)

    plt.figure()

    handles = plt.plot(rates, marker='o', markersize=10)
    plt.xlabel('Somatic current injection (nA)')
    plt.xticks(list(range(len(Ivals)))[::2], Ivals[::2])
    plt.ylabel('Frequency (Hz)')
    plt.legend(handles, params[0]['values'], title='dend Na', loc=2)
    plt.savefig('%s/%s/%s_fIcurve.png' % (dataFolder, batchLabel, batchLabel))
    plt.show()

def readFIplot():
    dataFolder = 'data/'
    batchLabel = 'batchNa'

    params, data = utils.readBatchData(dataFolder, batchLabel, loadAll=0, saveAll=1, vars=None, maxCombs=None)
    plotfINa(dataFolder, batchLabel, params, data)

# main code
if __name__ == '__main__':
    readFIplot()
    