import psutil
import subprocess
import time
import sys
import pandas as pd
import numpy as np
from datetime import datetime

from line_profiler import LineProfiler


def cpuLoadPower(samples, sampling_interval, * , write_freq=100, interval=None, stream=None):

    if stream == None:
        stream = sys.stdout

    temp_data = []

    fhandle = open('volt-amp-chrg-cpuLoad.csv', 'w')
    fhandle.write('Time,mV,mA,mAh,cpu_load\n')
    fhandle.close()

    for sample in range(samples):
        try:

            bash_string = subprocess.getoutput('./run_sys_profiler.sh')
            mV, mA, mAh = bash_string.split('\n')
        
        except:
            print('Something went wrong in the subprocess call. \nCheck the run_sys_profiler.sh script')
        
        cpu_load   = psutil.cpu_percent(interval)

        new_sample = {
            'Time':datetime.now().strftime('%H:%M:%S:%f'),
            'mV': mV,
            'mA': mA,
            'mAh':mAh,
            'cpu_load': cpu_load
        }

        temp_data.append(new_sample)

        if sample % write_freq == 0:
            # Uncomment the following lines to use to_csv method of 
            # Pandas instead of the write_to_file function given below
            # temp_df = pd.DataFrame(temp_data)
            # temp_df.to_csv('volt-amp-chrg-cpuLoad.csv',
            #                  mode='a',
            #                  header=False,
            #                  index=False)
            with open('volt-amp-chrg-cpuLoad.csv', 'a') as f:
                write_to_file(f, temp_data)
            temp_data = []
            stream.write('{} > {} samples processed\n'.format(datetime.now(), sample))

        time.sleep(sampling_interval)

def write_to_file(file_handle, list_of_dict):
    for entry in list_of_dict:
        file_handle.write(
            entry['Time'] +','+ 
            entry['mV'] +','+ 
            entry['mA'] +','+ 
            entry['mAh'] +','+ 
            str(entry['cpu_load']) +'\n'
            )

if __name__ == '__main__':
    lp = LineProfiler()
    lp_wrapper = lp(cpuLoadPower)
    lp_wrapper(30 , 1)
    lp.print_stats()

