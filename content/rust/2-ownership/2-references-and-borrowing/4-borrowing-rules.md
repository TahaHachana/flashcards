# Borrowing Rules

What are Rust’s core borrowing rules?

---

1. At most one mutable reference (`&mut T`) or any number of immutable references (`&T`) in a scope.  
2. References must always remain valid for their lifetimes.  
3. You cannot mix mutable and immutable borrows to the same data at the same time.
