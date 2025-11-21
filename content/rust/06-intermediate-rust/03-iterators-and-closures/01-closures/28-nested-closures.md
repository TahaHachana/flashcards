## Nested Closures

Can you have closures inside closures? How does variable capturing work with nested closures?

---

Yes, you can nest closures. Inner closures can capture variables from outer closures and the surrounding scope.

**Basic nesting:**
```rust
let x = 10;

let outer = || {
    let y = 20;
    
    let inner = || {
        println!("{} {}", x, y); // Captures both x and y
    };
    
    inner();
};

outer();
```

**Each closure captures independently:**
```rust
let x = 10;

let outer = move || {
    let y = 20;
    
    // Inner must also use move to capture y
    let inner = move || {
        println!("{} {}", x, y);
    };
    
    inner();
};
```

**Capture chain:**
```rust
let a = 1;

let first = || {
    let b = 2;
    
    let second = || {
        let c = 3;
        
        let third = || {
            println!("{} {} {}", a, b, c); // All visible
        };
        
        third();
    };
    
    second();
};
```

Each nested closure can access variables from all enclosing scopes. The same capture rules apply at each level.

