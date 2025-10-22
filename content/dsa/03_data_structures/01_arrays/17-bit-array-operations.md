## Bit Array Operations

What is a bit array and what are the four main bitwise operations?

---

Bit array: An array where each element is a single bit (0 or 1), used for space-efficient storage of boolean values.

Four main operations:
1. NOT - Invert all bits: NOT [0,1,0,1] = [1,0,1,0]
2. AND - Both bits must be 1: [0,1,0,1] AND [1,1,0,0] = [0,1,0,0]
3. OR - At least one bit is 1: [0,1,0,1] OR [1,1,0,0] = [1,1,0,1]
4. XOR - Exactly one bit is 1: [0,1,0,1] XOR [1,1,0,0] = [1,0,0,1]

Common uses: sets, bloom filters, boolean flags, bitmap graphics.

