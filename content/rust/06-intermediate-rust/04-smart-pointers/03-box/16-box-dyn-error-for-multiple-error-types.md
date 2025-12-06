## Box<dyn Error> for Multiple Error Types

Why is `Box<dyn Error>` useful for error handling, and how do you use it?

---

`Box<dyn Error>` allows a function to return different error types, since all errors implement the `Error` trait.

**The problem:**
```rust
use std::fs::File;
use std::io::Read;

// ❌ Can't return different error types
// fn read_data() -> Result<String, ???> {
//     let f = File::open("file.txt")?;  // io::Error
//     let n: i32 = "42".parse()?;       // ParseIntError
//     Ok(String::new())
// }
```

**The solution:**
```rust
use std::error::Error;
use std::fs::File;
use std::io::Read;

// ✅ Box<dyn Error> can hold any error type
fn read_data() -> Result<String, Box<dyn Error>> {
    let mut f = File::open("file.txt")?;  // io::Error
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    
    let n: i32 = "42".parse()?;  // ParseIntError
    
    Ok(s)
}
```

**Why this works:**
- Both errors implement `Error` trait
- `?` operator automatically boxes the errors
- Caller gets unified error type

**Use for:** Application-level error handling where you don't care about specific error types.

