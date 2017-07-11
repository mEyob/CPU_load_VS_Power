#!/bin/bash

echo $(/usr/sbin/system_profiler SPPowerDataType | grep 'Voltage (mV)' | egrep -o '[0-9]+')
echo $(/usr/sbin/system_profiler SPPowerDataType | grep 'Amperage (mA)' | egrep -o '[\-]*[0-9]+')
echo $(/usr/sbin/system_profiler SPPowerDataType | grep 'Charge Remaining (mAh)'| egrep -o '[0-9]+')
