## Why Memory Regions Exist

Why do programs use two different memory regions (stack and heap) instead of just one?

---

Different data has different needs. Some data is temporary and fixed-size (stack), while other data is long-lived or dynamic in size (heap). Using two specialized regions allows programs to handle both efficiently.

