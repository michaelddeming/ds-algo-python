"""What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?"""

start = 50
stop = 90
step = 10

# start at 50, end at 90 (exclusive), and step every 10 integers.
range_obj = range(start, stop, step)

# convert range object to a list to see values captured in the range.
print(list(range_obj))
