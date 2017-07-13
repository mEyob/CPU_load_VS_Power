## Intro

This repo illustrates the relationship between power consumption, CPU load, <br />
and CPU frequence of a laptop computer. Sample power consumption, CPU load  <br />
and frequency data is collected from a Macbook Pro having a Core i5 2.9 GHZ  <br />
processor powered by MacOS Seirra.

**Tools used:**

*MacOS SystemProfiler*: to collect battery discharge info., i.e., 
                          voltage and current readings.
                          
*[Intel Power Gadget](https://software.intel.com/en-us/articles/intel-power-gadget-20)*: CPU frequency and power consumption monitoring tool

**Python Libraries**

*psutil*: to gather CPU load at user-defined sampling intervals

*pandas and numpy*: to process the resulting data

*bokeh*: for plotting

I also wrote a small python program, *power_profile*, to automate the data collection
