## Standard Doc Sections

What are the standard documentation sections in Rust and when should you use each?

---

```rust
/// Brief description of function.
///
/// # Arguments
/// * `input` - The string to process
/// * `mode` - Processing mode
///
/// # Returns
/// Processed string result
///
/// # Examples
/// ```
/// let result = process("hello", Mode::Upper);
/// assert_eq!(result, "HELLO");
/// ```
///
/// # Panics
/// Panics if input is empty.
///
/// # Errors
/// Returns error if input contains invalid UTF-8.
///
/// # Safety
/// Safe to call from any context.
pub fn process(input: &str, mode: Mode) -> String
```

Sections:
- `# Examples` - Most important, always include
- `# Panics` - When function might panic
- `# Errors` - For Result-returning functions
- `# Safety` - For unsafe functions
- `# Arguments` - Complex parameters
- `# Returns` - Non-obvious returns

Examples are mandatory, others as needed.

