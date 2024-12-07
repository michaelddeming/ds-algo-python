"""What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0,−2,−4,−6,−8?"""

start = 8
stop = -10
step = -2

# start at 8, end at -10 (exclusive), and step every -2 integers.
range_obj = range(start, stop, step)


# convert range object to a list to see values captured in the range.
print(list(range_obj))
