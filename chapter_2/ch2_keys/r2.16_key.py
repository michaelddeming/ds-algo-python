"""Our Range class, from Section 2.3.5, relies on the formula
max(0, (stop - start + step - 1) // step) to compute the number of elements in the range. It is not immediately evident why this formula provides the correct calculation, even if assuming a positive step size. Justify this formula, in your own words."""


start = 10
stop = 0
step = -1

def func(start, stop, step):
    if step < 0:
        var = max(0, (stop - start - step -1) // step)
    else:
        var = max(0, (stop - start + step -1) // step)
    print(var)


func(start, stop, step)

# max(0,...) ensures that the value returned is never negative
# + step - 1 accounts for all step values in the bounds of start and stop

#WARNING this formula incorrectly returns the max elements in the range when provided a negative step. A if condition can be step to flip inverse the operator for 'step' on '+ step - 1' making it '-step -1'. 



