## Debugging Missing Module Errors

What are common causes of "cannot find module" errors, and how do you debug them?

---

**Common causes**:

1. **Forgot to declare**:
```rust
// ❌ No `mod helper;` in parent file
use helper::function;  // ERROR: cannot find `helper`
```
Fix: Add `mod helper;`

2. **Wrong file location**:
```rust
// In src/lib.rs
mod network;
// ERROR if file is at src/net/network.rs instead of src/network.rs
```
Fix: Move file to correct location

3. **Module not public**:
```rust
// src/network/mod.rs
mod server;  // Private!

// src/lib.rs
use network::server;  // ERROR: `server` is private
```
Fix: Change to `pub mod server;`

4. **Typo in module name**:
```rust
mod databse;  // Typo!
// Looking for databse.rs, but file is database.rs
```
Fix: Correct spelling

**Debug strategy**: Check file exists, in right place, and properly declared with `mod`.

