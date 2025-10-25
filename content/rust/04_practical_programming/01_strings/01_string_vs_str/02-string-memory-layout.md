## String Memory Layout

What three components make up a String's memory layout and where are they stored?

---

A String has three components stored on the stack:
1. Pointer to heap data
2. Length (bytes currently used)
3. Capacity (bytes allocated)

The actual string data lives on the heap.

