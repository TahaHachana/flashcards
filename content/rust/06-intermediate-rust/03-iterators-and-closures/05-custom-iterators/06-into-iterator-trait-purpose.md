## IntoIterator Trait Purpose

What is the IntoIterator trait? Why do we need it in addition to Iterator?

---

`IntoIterator` enables `for` loops and provides a way to convert types into iterators.

**Trait definition:**
```rust
pub trait IntoIterator {
    type Item;                              // What's yielded
    type IntoIter: Iterator<Item = Self::Item>;  // Iterator type
    
    fn into_iter(self) -> Self::IntoIter;  // Conversion method
}
```

**Purpose:**
- Allows `for` loops to work with your type
- Provides conversion to iterator
- Separates "can be iterated" from "is an iterator"

**Why both traits exist:**

**Iterator** = something that IS an iterator (has next())
**IntoIterator** = something that CAN BE CONVERTED to iterator

**For loop desugaring:**
```rust
// This code:
for item in collection {
    println!("{}", item);
}

// Desugars to:
let mut iter = collection.into_iter();
loop {
    match iter.next() {
        Some(item) => println!("{}", item),
        None => break,
    }
}
```

**Example implementation:**
```rust
struct BookCollection {
    books: Vec<String>,
}

// The iterator type
struct BookIntoIter {
    books: Vec<String>,
    index: usize,
}

impl Iterator for BookIntoIter {
    type Item = String;
    
    fn next(&mut self) -> Option<String> {
        if self.index < self.books.len() {
            let book = self.books[self.index].clone();
            self.index += 1;
            Some(book)
        } else {
            None
        }
    }
}

// IntoIterator implementation
impl IntoIterator for BookCollection {
    type Item = String;
    type IntoIter = BookIntoIter;
    
    fn into_iter(self) -> Self::IntoIter {
        BookIntoIter {
            books: self.books,
            index: 0,
        }
    }
}

// Now for loop works!
let collection = BookCollection { /* ... */ };
for book in collection {  // Calls into_iter()
    println!("{}", book);
}
```

**Key distinction:**
```rust
// Iterator - is an iterator
let mut iter = some_iterator;
iter.next();  // Has next() method

// IntoIterator - converts to iterator
let collection = some_collection;
let iter = collection.into_iter();  // Converts
iter.next();  // Now can call next()
```

IntoIterator is the "entry point" - it converts types into iterators so they can be used with for loops and iterator methods.

