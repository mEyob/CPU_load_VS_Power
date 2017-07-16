## Intro

This repo illustrates the relationship between power consumption, CPU load, <br />
and CPU frequency of a laptop computer. The subsequent analysis is based on a dataset 
collected from a 13-inch Macbook Pro running on a Core i5-5287U  <br />
processor with MacOS Seirra installed.

**Tools used:**

*MacOS SystemProfiler*: to collect battery discharge info., i.e., 
                          voltage and current readings.
                          
*[Intel Power Gadget](https://software.intel.com/en-us/articles/intel-power-gadget-20)*: CPU frequency and power consumption monitoring tool

**Python Libraries**

*psutil*: to gather CPU load at user-defined sampling intervals

*pandas and numpy*: to process the resulting data

*bokeh*: for plotting

I also wrote a small python program, *power_profile*, to automate the data collection.
Start [here](analysis.md) for a short description of the project and analysis of the collected data.
