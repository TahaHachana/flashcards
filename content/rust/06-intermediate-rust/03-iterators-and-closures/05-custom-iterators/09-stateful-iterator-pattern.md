## Stateful Iterator Pattern

Show how to create an iterator that maintains state and transforms elements based on that state (running sum example).

---

Stateful iterators track accumulated state across iterations to transform elements.

**Running sum iterator:**
```rust
struct RunningSum<I> {
    inner: I,
    sum: i32,
}

impl<I> RunningSum<I> {
    fn new(inner: I) -> Self {
        RunningSum { inner, sum: 0 }
    }
}

impl<I> Iterator for RunningSum<I>
where
    I: Iterator<Item = i32>,
{
    type Item = i32;
    
    fn next(&mut self) -> Option<i32> {
        match self.inner.next() {
            Some(n) => {
                self.sum += n;  // Accumulate state
                Some(self.sum)   // Return accumulated value
            }
            None => None,
        }
    }
}

// Usage
let values = vec![1, 2, 3, 4, 5];
let running = RunningSum::new(values.into_iter());
let result: Vec<_> = running.collect();
// [1, 3, 6, 10, 15]
// Each element is sum of all previous
```

**Running average:**
```rust
struct RunningAverage<I> {
    inner: I,
    sum: f64,
    count: usize,
}

impl<I> Iterator for RunningAverage<I>
where
    I: Iterator<Item = f64>,
{
    type Item = f64;
    
    fn next(&mut self) -> Option<f64> {
        match self.inner.next() {
            Some(n) => {
                self.sum += n;
                self.count += 1;
                Some(self.sum / self.count as f64)
            }
            None => None,
        }
    }
}

// Usage
let temps = vec![70.0, 72.0, 68.0, 75.0];
let avg = RunningAverage {
    inner: temps.into_iter(),
    sum: 0.0,
    count: 0,
};
let result: Vec<_> = avg.collect();
// [70.0, 71.0, 70.0, 71.25]
```

**Difference from previous:**
```rust
struct Differences<I> {
    inner: I,
    previous: Option<i32>,
}

impl<I> Iterator for Differences<I>
where
    I: Iterator<Item = i32>,
{
    type Item = i32;
    
    fn next(&mut self) -> Option<i32> {
        match self.inner.next() {
            Some(current) => {
                let diff = match self.previous {
                    Some(prev) => current - prev,
                    None => 0,  // First element
                };
                self.previous = Some(current);
                Some(diff)
            }
            None => None,
        }
    }
}

// Usage
let values = vec![10, 15, 13, 20, 18];
let diffs = Differences {
    inner: values.into_iter(),
    previous: None,
};
let result: Vec<_> = diffs.collect();
// [0, 5, -2, 7, -2]
```

**Key pattern:**
1. Store state in iterator struct
2. Update state in `next()`
3. Use state to transform current element
4. Wrap another iterator for composition

This pattern enables powerful transformations while maintaining iterator composability.

