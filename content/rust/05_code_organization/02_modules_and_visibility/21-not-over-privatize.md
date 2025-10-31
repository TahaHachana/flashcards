## Why Not Over-Privatize

What's the balance between privacy and accessibility in Rust?

---

**Don't over-privatize** - the goal is a clean API, not maximum restrictions.

**Good practice**:
- Private by default is about preventing *accidental* exposure, not hiding everything
- Make things public if they're meant to be used
- Keep implementation details private
- Expose a clear, useful interface

**Example of good balance**:
```rust
pub mod parser {
    // Public API - what users need
    pub struct Parser { /* ... */ }
    pub fn parse(input: &str) -> Result<Ast, Error> { /* ... */ }
    
    // Private helpers - internal details
    fn tokenize(input: &str) -> Vec<Token> { /* ... */ }
    fn validate_syntax(tokens: &[Token]) -> Result<(), Error> { /* ... */ }
}
```

**Goal**: Clean, useful public interface + hidden complexity.

