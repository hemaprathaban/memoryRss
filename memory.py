import matplotlib.pyplot as plt 
import numpy as np
import random

_FIELDS = ['VmRss', 'Name']
mem=['VmRSS']

def get_memory():
    '''
    returns the current and peak, real and virtual memories
    used by the calling linux python process, in Bytes
    '''
    
    # read in process info
    with open('filepath', 'r') as file:
        lines = file.read().split('\n')


    # container of memory values (_FIELDS)
    values = []
    height = []
    valname={}
    proc = {}
    procnames = []
    name = {}
    val = {}
    # check all process info fiels
    for line in lines:
        
        if ':' in line :
            name  = line.split(':')[0]
            val = line.split(':')[1]

            # collect relevant memory fields
            if name in mem:
                #line = line.replace('\t', '').replace('[', '').replace(']', '').replace(' ', '')
                valname[name] = int(val.strip().split(' ')[0])
                megabyte = float(0.000976562)
                memorysize = valname[name] * megabyte
                values.append(memorysize)
            if name == 'Name':
                proc[name] = val.strip().split(' ')[0]
                procnames.append(proc[name])
    height =  values
    bars = procnames
    y_pos = np.arange(len(bars))
    plt.figure(figsize=(35,20))
    rgb = np.random.rand(3, )
    plt.barh(y_pos, height, color = 'rgbkymc' )

    plt.yticks(y_pos, bars, fontsize=25)
    plt.ylabel('Process Name', fontsize=20)
    plt.xlabel('VmRSS in MB', fontsize=20)

    plt.xticks(fontsize=25)
    plt.savefig('memoryVmRSS.svg')
    #plt.show()

  
    return  values


if __name__ == '__main__':

    get_memory()

    
