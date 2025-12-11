## Sharing Data with Rc - Practical Example

Demonstrate how `Rc` solves the problem of sharing expensive data between multiple structs without cloning.

---

**Without Rc (doesn't work):**
```rust
struct City {
    name: String,
    history: String,  // Expensive data
}

struct CityData {
    names: Vec<String>,
    histories: Vec<String>,
}

let calgary = City {
    name: "Calgary".to_string(),
    history: "Long history...".to_string(),
};

let data = CityData {
    names: vec![calgary.name],      // Takes ownership!
    histories: vec![calgary.history],  // Takes ownership!
};
// ❌ Error: calgary fields moved
```

**With Rc (works):**
```rust
use std::rc::Rc;

struct City {
    name: Rc<String>,
    history: Rc<String>,
}

struct CityData {
    names: Vec<Rc<String>>,
    histories: Vec<Rc<String>>,
}

let name = Rc::new("Calgary".to_string());
let history = Rc::new("Long history...".to_string());

let calgary = City {
    name: Rc::clone(&name),
    history: Rc::clone(&history),
};

let data = CityData {
    names: vec![Rc::clone(&name)],
    histories: vec![Rc::clone(&history)],
};

// ✅ Both can access the data!
println!("{}", calgary.history);
println!("Count: {}", Rc::strong_count(&history));  // 3
```

