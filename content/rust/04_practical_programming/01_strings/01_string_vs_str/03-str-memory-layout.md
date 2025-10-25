## &str Memory Layout

What is a &str's memory layout and why doesn't it have a capacity field?

---

A &str is a fat pointer with two components:
1. Pointer to the UTF-8 data
2. Length (number of bytes)

It has no capacity field because &str is a fixed-size view into existing data - it can't grow or shrink. It's just a window into string data, not a growable buffer.

