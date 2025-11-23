## Iterator Wrapper Pattern

Show the pattern for creating an iterator that wraps another iterator (similar to standard library adaptors).

---

Iterator wrappers delegate to an inner iterator while adding behavior.

**Basic wrapper pattern:**
```rust
struct MyMap<I, F> {
    iter: I,     // Wrapped iterator
    func: F,     // Transformation function
}

impl<B, I, F> Iterator for MyMap<I, F>
where
    I: Iterator,
    F: FnMut(I::Item) -> B,
{
    type Item = B;
    
    fn next(&mut self) -> Option<B> {
        // Get next from inner, apply transformation
        self.iter.next().map(&mut self.func)
    }
}

// Constructor function
fn my_map<I, F, B>(iter: I, func: F) -> MyMap<I, F>
where
    I: Iterator,
    F: FnMut(I::Item) -> B,
{
    MyMap { iter, func }
}

// Usage
let doubled = my_map(vec![1, 2, 3].into_iter(), |x| x * 2);
let result: Vec<_> = doubled.collect();
// [2, 4, 6]
```

**Wrapper with state:**
```rust
struct Enumerate<I> {
    iter: I,
    count: usize,
}

impl<I> Iterator for Enumerate<I>
where
    I: Iterator,
{
    type Item = (usize, I::Item);
    
    fn next(&mut self) -> Option<(usize, I::Item)> {
        match self.iter.next() {
            Some(item) => {
                let index = self.count;
                self.count += 1;
                Some((index, item))
            }
            None => None,
        }
    }
}
```

**Logging wrapper (side effects):**
```rust
struct Logging<I> {
    iter: I,
    count: usize,
}

impl<I> Iterator for Logging<I>
where
    I: Iterator,
    I::Item: std::fmt::Debug,
{
    type Item = I::Item;
    
    fn next(&mut self) -> Option<I::Item> {
        match self.iter.next() {
            Some(item) => {
                self.count += 1;
                println!("Item #{}: {:?}", self.count, item);
                Some(item)
            }
            None => {
                println!("Iterator exhausted after {} items", self.count);
                None
            }
        }
    }
}
```

**Extension trait pattern:**
```rust
trait IteratorExt: Iterator {
    fn my_map<F, B>(self, f: F) -> MyMap<Self, F>
    where
        Self: Sized,
        F: FnMut(Self::Item) -> B,
    {
        MyMap { iter: self, func: f }
    }
    
    fn logging(self) -> Logging<Self>
    where
        Self: Sized,
        Self::Item: std::fmt::Debug,
    {
        Logging { iter: self, count: 0 }
    }
}

// Implement for all iterators
impl<I: Iterator> IteratorExt for I {}

// Usage - looks like built-in methods!
let result: Vec<_> = vec![1, 2, 3]
    .into_iter()
    .my_map(|x| x * 2)
    .logging()
    .collect();
```

**Key pattern elements:**
1. Generic over inner iterator `I: Iterator`
2. Store inner iterator in struct
3. Delegate `next()` to inner
4. Add transformation/filtering/side effects
5. Return transformed result

This is exactly how standard library adaptors (map, filter, etc.) work!

