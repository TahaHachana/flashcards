## Map Adaptor Deep Dive

What does `.map()` do? Show examples of type transformation and explain why multiple maps fuse efficiently.

---

`.map()` transforms each element through a closure, creating one-to-one correspondence.

**Signature:**
```rust
fn map<B, F>(self, f: F) -> Map<Self, F>
where
    F: FnMut(Self::Item) -> B
```

**Basic transformation:**
```rust
let doubled = vec![1, 2, 3].iter()
    .map(|&x| x * 2)
    .collect::<Vec<_>>();
// [2, 4, 6]
```

**Type transformation:**
```rust
let strings = vec![1, 2, 3].iter()
    .map(|&n| format!("Number {}", n))
    .collect::<Vec<String>>();
// ["Number 1", "Number 2", "Number 3"]
```

**Multiple maps fuse:**
```rust
// This:
iter.map(|x| x * 2).map(|x| x + 1).map(|x| x.to_string())

// Compiles to same code as:
iter.map(|x| ((x * 2) + 1).to_string())
```

**Why fusion works:**
Each element flows through entire chain before next element starts. The compiler inlines all closures into a single operation per element.

**Common pattern - struct field extraction:**
```rust
let names: Vec<String> = people.iter()
    .map(|p| p.name.clone())
    .collect();
```

Map is the most fundamental transformation adaptor.

