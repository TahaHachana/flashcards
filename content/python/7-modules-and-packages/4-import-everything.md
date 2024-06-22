# Import All Definitions From a Module

In Python, you can import all definitions (functions, classes, variables) from a module using the `*` operator. This allows you to use all the definitions from the module without having to prefix them with the module name.

---

```python
# Import all functions and variables from the math module
from math import *

# Use the imported functions directly
result = sqrt(16)
print(result)  # Output: 4.0

# Access the imported constant
print(pi)  # Output: 3.141592653589793
```