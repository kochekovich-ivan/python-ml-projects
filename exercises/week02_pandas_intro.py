3 = pd.Series(a, ["first", "second", "third", "fourth"])
print(ser3)
print(ser3["first"])  # access by label → 1
print(ser3[0])        # access by position → 1

# create Series from dict
d = {"first": 1, "second": 2}
ser4 = pd.Series(d)
print(ser4)
print(ser4["first"])  # access by key
print(ser4[1])        # access by position

# arithmetic with Series
ser5 = pd.Series(a)
print(ser5 + 2)       # add a number to each element
print(ser5)           # original Series unchanged
print(ser5 > 2)       # boolean mask (True/False)
print(ser5.max())     # max value
print(ser5.min())     # min value
print(ser5.sum())     # sum of elements
print(sorted(ser5))   # sorted as Python list
print(list(ser5))     # convert to regular list

# attributes and methods
print(ser.values)                  # numpy array of values
print(ser.index)                   # index object
print(ser.size)                    # number of elements
print(ser.is_unique)               # check if all values are unique
print(ser.is_monotonic_increasing) # check if sorted ascending
print(ser.is_monotonic_decreasing) # check if sorted descending
print(ser.product())               # product of all elements
print(ser.mean())                  # mean of elements
print(ser.dtype)                   # data type of elements
print(ser.head(2))                 # first 2 rows
print(ser.tail(2))                 # last 2 rows
print(ser.take([1, 3]))            # take by positions 1 and 3
print(ser[1:2])                    # slice from 1 to 2 (exclusive)
print(ser[:3])                     # first 3 elements
print(ser[1:])                     # from index 1 to the end
print(ser[::2])                    # every second element
print(ser[::-1])                   # reversed Series

# position-based indexing
print(ser.iloc[2])                 # single element at pos 2
print(ser.iloc[[1, 3]])            # multiple elements at positions 1 and 3

# label-based indexing (works if labels exist)
print(ser.loc[2])                  # element at label 2
print(ser.loc[[1, 3]])             # elements at labels 1 and 3

# sorting
print(ser.sort_values())           # return sorted values
print(ser.sort_values(ascending=False)) # sorted descending

# apply a custom function to each element
def sign(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"

print(ser.apply(sign))
