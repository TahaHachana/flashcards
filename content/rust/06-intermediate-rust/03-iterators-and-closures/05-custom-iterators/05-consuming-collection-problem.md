## Consuming Collection Problem

What's the problem with implementing Iterator directly on a collection? Show the issue and solution.

---

Implementing Iterator directly on a collection consumes it on first iteration.

**Problem - consuming the collection:**
```rust
struct BookCollection {
    books: Vec<String>,
}

// ❌ Implementing Iterator directly
impl Iterator for BookCollection {
    type Item = String;
    
    fn next(&mut self) -> Option<String> {
        self.books.pop()  // Removes from collection!
    }
}

// Usage issue:
let mut books = BookCollection {
    books: vec!["Book 1".to_string(), "Book 2".to_string()],
};

for book in books {
    println!("{}", book);
}
// books is now EMPTY and can't be used again!
```

**Solution - separate iterator type:**
```rust
struct BookCollection {
    books: Vec<String>,
}

// Separate iterator struct
struct BookIter<'a> {
    books: &'a [String],
    index: usize,
}

impl<'a> Iterator for BookIter<'a> {
    type Item = &'a String;
    
    fn next(&mut self) -> Option<&'a String> {
        if self.index < self.books.len() {
            let book = &self.books[self.index];
            self.index += 1;
            Some(book)
        } else {
            None
        }
    }
}

impl BookCollection {
    fn iter(&self) -> BookIter {
        BookIter {
            books: &self.books,
            index: 0,
        }
    }
}
```

**Now non-consuming:**
```rust
let collection = BookCollection {
    books: vec!["Book 1".to_string(), "Book 2".to_string()],
};

// First iteration
for book in collection.iter() {
    println!("{}", book);
}

// Collection still available!
for book in collection.iter() {
    println!("{}", book);
}

// Can still access collection
println!("Have {} books", collection.books.len());
```

**Pattern benefits:**
- Original collection preserved
- Can iterate multiple times
- Follows standard library conventions (Vec::iter(), etc.)
- Can provide iter(), iter_mut(), and into_iter()

**Standard library follows this:**
```rust
// Vec doesn't implement Iterator
// Instead provides methods returning iterators:
vec.iter()       // Returns Iter<'_, T>
vec.iter_mut()   // Returns IterMut<'_, T>  
vec.into_iter()  // Consumes Vec, returns IntoIter<T>
```

Always use separate iterator types to avoid consuming collections.

