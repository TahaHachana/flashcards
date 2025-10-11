## Direct vs Indirect Recursion

What is the difference between direct recursion and indirect recursion?

---

**Direct Recursion**: A procedure P contains a call statement to itself
```
procedure P()
    ...
    P()  // calls itself
    ...
```

**Indirect Recursion**: Procedure P calls another procedure that eventually results in a call back to P
```
procedure P()     procedure Q()
    ...               ...
    Q()               P()
    ...               ...
```

Both are valid recursion forms requiring base cases and progress toward base case.

