## Why Data Structure Choice Matters

Using the telephone directory example, explain why the choice of data structure organization matters for algorithm efficiency.

---

In a telephone directory sorted alphabetically by name, finding a person is efficient because you can jump to the approximate location and scan locally.

If the same directory were sorted by subscription date, you would have to search every entry sequentially from start to finish.

Same data, same search algorithm, but different organization leads to dramatically different performance. This demonstrates that good algorithm design must go hand in hand with appropriate data structures.

