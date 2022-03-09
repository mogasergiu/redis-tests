#!/usr/bin/env python3

import matplotlib.pyplot as plt
from datetime import datetime

with open("strace-syscalls") as file:
    syscalls = file.read().splitlines()

with open("strace-timestamps") as file:
    timestamps = file.read().splitlines()

fmt = "%H:%M:%S.%f"
last_timestamp = datetime.strptime(timestamps[-1], fmt)

delta_timestamps = []
for t in timestamps:
    delta_timestamps.append(float((str((last_timestamp - datetime.strptime(t, fmt)).total_seconds()))))

delta_timestamps = list(reversed(delta_timestamps))

plt.plot(delta_timestamps, syscalls, 'o', color='black')
plt.show()
