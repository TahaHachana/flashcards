## Cycle Infinite Repetition

What does `.cycle()` do? Show a practical example and explain why `.take()` is essential.

---

`.cycle()` repeats an iterator infinitely by cloning and restarting when it reaches the end.

**Signature:**
```rust
fn cycle(self) -> Cycle<Self>
where
    Self: Clone
```

**Basic usage:**
```rust
let pattern: Vec<i32> = vec![1, 2, 3]
    .iter()
    .cycle()
    .take(10)  // MUST limit!
    .copied()
    .collect();
// [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
```

**Alternating labels:**
```rust
let labels = ["even", "odd"].iter().cycle();
let labeled: Vec<_> = (0..6)
    .zip(labels)
    .map(|(num, label)| format!("{}: {}", num, label))
    .collect();
// ["0: even", "1: odd", "2: even", "3: odd", "4: even", "5: odd"]
```

**Round-robin distribution:**
```rust
let servers = vec!["server1", "server2", "server3"];
let assignments: Vec<_> = tasks.iter()
    .zip(servers.iter().cycle())
    .map(|(task, server)| (task.clone(), *server))
    .collect();
// Distributes tasks evenly across servers
```

**Animation frames:**
```rust
let frames = [Frame1, Frame2, Frame3, Frame4];
let animation = frames.iter()
    .cycle()
    .take(total_frame_count)
    .cloned();
```

**⚠️ CRITICAL WARNING:**
```rust
// INFINITE LOOP - program hangs forever!
// vec![1, 2, 3].iter().cycle().for_each(|x| println!("{}", x));

// CORRECT - must limit
vec![1, 2, 3].iter().cycle().take(10).for_each(|x| println!("{}", x));
```

**Requirement:** Inner iterator must be `Clone` so it can restart.

Always use with `.take()`, `.take_while()`, or `.zip()` with finite iterator to prevent infinite loops!

