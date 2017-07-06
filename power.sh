#!/bin/bash

Voltage=$(/usr/sbin/system_profiler SPPowerDataType | grep 'Voltage (mV)' | egrep -o '[0-9]+')
Amperage=$(/usr/sbin/system_profiler SPPowerDataType | grep 'Amperage (mA)' | egrep -o '[\-]*[0-9]+')
RemCharge=$(/usr/sbin/system_profiler SPPowerDataType | grep 'Charge Remaining (mAh)'| egrep -o '[0-9]+')

t=$(date -j -f "%a %b %d %T %Z %Y" "`date`" "+%s")

printf '%s\t%s\t%s\t%s\n' "$t" "$Voltage" "$Amperage" "$RemCharge" >> volt-amp.txt
