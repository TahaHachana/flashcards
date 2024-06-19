# Flush Parameter

The `flush` parameter in the `print()` function is used to forcibly flush the stream. By default, the stream is not flushed.

```python
import time

for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)
# Output: 0 1 2 3 4 (printed with a delay of 1 second between each number)
```