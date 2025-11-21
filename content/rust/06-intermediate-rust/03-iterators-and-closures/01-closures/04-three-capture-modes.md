## Three Capture Modes

What are the three ways closures can capture variables from their environment? List them from least to most restrictive.

---

Closures automatically choose the most restrictive mode that allows them to work:

1. **By immutable reference (`&T`)** - Read-only access
   ```rust
   let x = String::from("hello");
   let read = || println!("{}", x); // Borrows &x
   ```

2. **By mutable reference (`&mut T`)** - Read-write access
   ```rust
   let mut count = 0;
   let mut inc = || count += 1; // Borrows &mut count
   ```

3. **By value (`T`)** - Takes ownership
   ```rust
   let data = vec![1, 2, 3];
   let consume = || drop(data); // Moves data
   ```

The compiler selects the least restrictive mode that satisfies the closure's needs.

