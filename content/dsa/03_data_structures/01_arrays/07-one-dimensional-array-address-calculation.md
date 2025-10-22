## One-Dimensional Array Address Calculation

What is the formula for calculating the address of element A[i] in a one-dimensional array A[l:u] with base address α?

---

Address(A[i]) = α + (i - l)

Where:
- α = base address
- i = index of desired element
- l = lower bound

Example: A[1:17] with α = 100
Address of A[7] = 100 + (7 - 1) = 106

Example: A[-2:23] with α = 100
Address of A[16] = 100 + (16 - (-2)) = 118

