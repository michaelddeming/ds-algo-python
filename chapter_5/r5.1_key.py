"""Execute the experiment from Code Fragment 5.1 and compare the results
on your system to those we report in Code Fragment 5.2."""


import sys

data = []

for k in range(6):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a,b))
    data.append(None)

# Length:   0; Size in bytes:   56
# Length:   1; Size in bytes:   88
# Length:   2; Size in bytes:   88
# Length:   3; Size in bytes:   88
# Length:   4; Size in bytes:   88
# Length:   5; Size in bytes:  120
# Length:   6; Size in bytes:  120
# Length:   7; Size in bytes:  120
# Length:   8; Size in bytes:  120
# Length:   9; Size in bytes:  184
# Length:  10; Size in bytes:  184
# Length:  11; Size in bytes:  184
# Length:  12; Size in bytes:  184
# Length:  13; Size in bytes:  184
# Length:  14; Size in bytes:  184
# Length:  15; Size in bytes:  184
# Length:  16; Size in bytes:  184
# Length:  17; Size in bytes:  248
# Length:  18; Size in bytes:  248
# Length:  19; Size in bytes:  248
# Length:  20; Size in bytes:  248
# Length:  21; Size in bytes:  248
# Length:  22; Size in bytes:  248
# Length:  23; Size in bytes:  248
# Length:  24; Size in bytes:  248
# Length:  25; Size in bytes:  312
# Length:  26; Size in bytes:  312

# Observation: My system, Apple Macbook Pro M3 Pro 2023, uses slightly less memory for the same capacity as that of the book example, interesting?




