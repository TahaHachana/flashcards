## Three Purposes of Trait Bounds

What are the three key purposes of trait bounds?

---

1. **Enable operations**: Let you call trait methods on generic types

   ```rust
   fn f<T: Clone>(x: T) { x.clone(); }  // Can call .clone()
   ```

2. **Compile-time guarantees**: Ensure types have required capabilities before code runs

   ```rust
   fn f<T: Display>(x: T) { println!("{}", x); }  // Guaranteed to work
   ```

3. **Documentation**: Make function requirements explicit and clear

   ```rust
   fn compare<T: PartialOrd>(a: T, b: T)  // Clear: T must be orderable
   ```

Trait bounds make generic code both safe and flexible.

