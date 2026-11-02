import numpy as np

# 1. Creating Arrays
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:\n", arr_1d)

# Creating a 2D array (Matrix)
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array (Matrix A):\n", matrix_a)

# 2. Inspecting Array Properties
print("\n--- Array Properties ---")
print("Shape of Matrix A:", matrix_a.shape)     # Dimensions (rows, columns)
print("Data type of Matrix A:", matrix_a.dtype) # Type of elements
print("Total elements:", matrix_a.size)        # Number of elements

# 3. Built-in Array Generators
print("\n--- Built-in Generators ---")
print("Array of Zeros:\n", np.zeros((2, 3)))      # 2x3 matrix of 0s
print("Array of Ones:\n", np.ones((2, 2)))        # 2x2 matrix of 1s
print("Sequence (arange):\n", np.arange(0, 10, 2)) # From 0 to 8 with step 2
print("Linearly Spaced (linspace):\n", np.linspace(0, 1, 5)) # 5 points from 0 to 1

# 4. Basic Mathematical Operations (Element-wise)
print("\n--- Basic Math (Element-wise) ---")
matrix_b = np.array([[10, 20, 30], [40, 50, 60]])
print("Matrix B:\n", matrix_b)
print("Addition (A + B):\n", matrix_a + matrix_b)
print("Multiplication by Scalar (A * 2):\n", matrix_a * 2)

# 5. Statistical and Aggregate Functions
print("\n--- Aggregations ---")
print("Sum of all elements in A:", matrix_a.sum())
print("Mean (Average) of A:", matrix_a.mean())
print("Maximum value in A:", matrix_a.max())
print("Column-wise sums of A:", matrix_a.sum(axis=0)) # Sum down columns

# 6. Slicing and Indexing
print("\n--- Slicing & Indexing ---")
# Get specific element (row 1, column 2 -> 0-indexed)
print("Element at row 1, col 2:", matrix_a[1, 2])
# Slice row 0, columns 1 and 2
print("Slice of Row 0 (cols 1-2):", matrix_a[0, 1:3])

# 7. Matrix Manipulation
print("\n--- Matrix Manipulation ---")
print("Transpose of Matrix A:\n", matrix_a.T)