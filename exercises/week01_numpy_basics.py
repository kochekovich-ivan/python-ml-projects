import numpy as np

# TASKS WEEK 1


# Create an array with numbers from 1 to 20.
arr = np.arange(1,21)

# Create an array of 15 zeros and another one of 15 ones.
zeros = np.zeros(15)
ones = np.ones(15)

# Create an array with numbers from 0 to 1 with step 0.05.
from0to1 = np.arange(0, 1.05, 0.05)

# Generate a 5×5 identity matrix.
matrix5x5 = np.identity(5)

# Create a 3×3 matrix filled with the value 7.
matrix3x3 = np.full((3, 3), 7)

# Create a 10×10 matrix of random floats between 0 and 1.
rand10x10 = np.random.rand(10, 10)

# Create an array of integers from 100 to 200, then convert it to float64.
from100to200 = np.arange(100, 201)
np.float64(from100to200)

# Create a 5×5 diagonal matrix with values [1, 2, 3, 4, 5] on the diagonal.
diag5x5 = np.diag([1,2,3,4,5])

# Create a 1D array of 100 equally spaced numbers between 0 and 10.
space100 = np.linspace(0, 10, 100)

# Generate an array of powers of 2 from 2^0 to 2^10.
arrayOfPowers = np.power(2, np.arange(11))

# Create a 3×4 matrix using arange() and reshape it.
matrix3x4 = np.arange(12).reshape(3, 4)

# Create an array of integers from -50 to 50 and find all positive values.
from_50to50 = np.arange(-50, 51)
positive_values = from_50to50[from_50to50 > 0]

# Create two arrays a and b (length 5 each) and compute: a + b, a - b, a * b, a / b
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
div_ab = a / b

# Create a 1D array of 20 random integers between 0 and 100, then:
# Find the maximum and minimum.
# Compute the mean and standard deviation.

rand20 = np.random.randint(0, 101, size=20)
max_val = rand20.max()
min_val = rand20.min()
mean_val = rand20.mean()
std_val = rand20.std()

# Create a 5×5 random matrix and find:
#The sum of each row.
#The sum of each column.

rand5x5 = np.random.rand(5, 5)
row_sums = rand5x5.sum(axis=1)
col_sums = rand5x5.sum(axis=0)