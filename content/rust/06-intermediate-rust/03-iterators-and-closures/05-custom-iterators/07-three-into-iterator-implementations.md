## Three IntoIterator Implementations

What are the three standard IntoIterator implementations? Show the pattern for each.

---

Complete iterator support requires three IntoIterator implementations for different ownership scenarios.

**The three implementations:**

**1. By value (consumes collection):**
```rust
impl IntoIterator for BookCollection {
    type Item = String;
    type IntoIter = BookIntoIter;
    
    fn into_iter(self) -> Self::IntoIter {
        BookIntoIter {
            books: self.books,  // Takes ownership
            index: 0,
        }
    }
}

// Usage: moves collection
for book in collection {  // Consumes collection
    println!("{}", book);
}
// collection no longer available
```

**2. By immutable reference (borrows collection):**
```rust
impl<'a> IntoIterator for &'a BookCollection {
    type Item = &'a String;
    type IntoIter = std::slice::Iter<'a, String>;
    
    fn into_iter(self) -> Self::IntoIter {
        self.books.iter()  // Borrows
    }
}

// Usage: borrows collection
for book in &collection {  // Non-consuming
    println!("{}", book);
}
// collection still available
```

**3. By mutable reference (borrows mutably):**
```rust
impl<'a> IntoIterator for &'a mut BookCollection {
    type Item = &'a mut String;
    type IntoIter = std::slice::IterMut<'a, String>;
    
    fn into_iter(self) -> Self::IntoIter {
        self.books.iter_mut()  // Mutable borrow
    }
}

// Usage: mutable iteration
for book in &mut collection {  // Mutable borrow
    book.push_str(" - Read");
}
// collection still available (was mutated)
```

**Usage comparison:**
```rust
let mut collection = BookCollection { /* ... */ };

// 1. Borrow immutably
for book in &collection {
    println!("{}", book);
}

// 2. Borrow mutably
for book in &mut collection {
    *book = book.to_uppercase();
}

// 3. Consume
for book in collection {
    println!("{}", book);
}
// collection moved, no longer available
```

**Pattern template:**
```rust
// By value
impl IntoIterator for T { /* ... */ }

// By reference
impl<'a> IntoIterator for &'a T { /* ... */ }

// By mutable reference
impl<'a> IntoIterator for &'a mut T { /* ... */ }
```

**Standard library follows this:**
```rust
// Vec has all three
for x in vec { }       // Moves
for x in &vec { }      // Borrows
for x in &mut vec { }  // Mut borrows
```

Implementing all three provides maximum flexibility and matches standard library conventions.

