import matplotlib.pyplot as plt 
import numpy as np


_FIELDS = ['VmSize', 'Name']
mem=['VmSize']
pname1 =['Name']

def get_memory():
    '''
    returns the current and peak, real and virtual memories
    used by the calling linux python process, in Bytes
    '''
    
    # read in process info
    ln = 100
    with open('/home/hema/Downloads/test1.txt', 'r') as file:
        lines = file.read().split('\n')


    # container of memory values (_FIELDS)
    values = []
    height = []
    values1={}
    procname = {}
    pname = {}
    pnames = []
    name = {}
    val = {}
    # check all process info fiels
    for line in lines:
        
        if ':' in line :
            name  = line.split(':')[0]
            #print (name)
            val = line.split(':')[1]
            #print (val)

            # collect relevant memory fields
            if name == 'Name':
                procname[name] = val.strip().split(' ')[0]
                pnames.append(procname[name])
            if name in mem:
                #line = line.replace('\t', '').replace('[', '').replace(']', '').replace(' ', '')
                values1[name] = int(val.strip().split(' ')[0])
                megabyte = float(0.000976562)
                memorysize = values1[name] * megabyte
                values.append(memorysize)
    height =  values
    print (len(height))
    print (height)
    bars = pnames
    print  len((bars))
    y_pos = np.arange(len(bars))
    plt.barh(y_pos, height)
    plt.yticks(y_pos, bars)

    plt.show()

  
    return  values


if __name__ == '__main__':

    get_memory()

    
