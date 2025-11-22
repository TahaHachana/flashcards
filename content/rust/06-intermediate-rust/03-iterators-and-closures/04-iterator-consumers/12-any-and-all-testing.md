## Any and All Testing

What do `.any()` and `.all()` do? How do they short-circuit, and what's their relationship?

---

Test predicates across iterators, returning boolean results with short-circuiting.

**Any - true if ANY element matches:**
```rust
fn any<F>(&mut self, f: F) -> bool
where F: FnMut(Self::Item) -> bool
```

```rust
let has_even = vec![1, 3, 5, 6, 9].iter()
    .any(|&x| x % 2 == 0);
// true (6 is even - stops checking after finding it)
```

**All - true if ALL elements match:**
```rust
fn all<F>(&mut self, f: F) -> bool
where F: FnMut(Self::Item) -> bool
```

```rust
let all_positive = vec![1, 2, 3, 4].iter()
    .all(|&x| x > 0);
// true

let all_positive = vec![1, 2, -3, 4].iter()
    .all(|&x| x > 0);
// false (stops at -3, doesn't check 4)
```

**Short-circuiting:**
- `.any()` stops at first `true`
- `.all()` stops at first `false`

```rust
// Only checks 0-101, not all million
(0..1_000_000).any(|x| x > 100)  // true

// Only checks 0-2, stops at -3
vec![1, 2, -3, 4, 5].iter().all(|&x| x > 0)  // false
```

**Relationship (De Morgan's laws):**
```rust
// These are equivalent
!iter.any(|x| condition(x))
iter.all(|x| !condition(x))

// And
!iter.all(|x| condition(x))
iter.any(|x| !condition(x))
```

**Edge case - empty iterator:**
```rust
Vec::<i32>::new().iter().any(|&x| x > 0)  // false
Vec::<i32>::new().iter().all(|&x| x > 0)  // true (vacuous truth)
```

